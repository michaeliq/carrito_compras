from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

from . import sell
from app.models import Producto

@sell.route('/home/')
def home():
    productos = Producto.query.all()
    return render_template('sell/home_page.html',items = productos)

@sell.route('/compra/<string:nombrep>/',methods=['GET','POST'])
def compra(nombrep):
    form = FormAgregarProducto()
    if form.validate_on_submit():
        #comprobar si el usuario hizo login
        if current_user.is_anonymous:
            print('necesitar iniciar sesión')
            return redirect(url_for('auth.login'))
        producto = {'nombreProducto':form.nombreProducto.data,
                'detalle':[{
                'cantidad':form.cantidad.data,
                'precio':form.precio.data}]
                }
        id_usuario = current_user.id
        carrito = Carrito.query.filter_by(usuario=id_usuario).first()
        if carrito:
            productos = json.loads(carrito.productos)
            valor_total = productos['precio'] + (producto['detalle'][0]['precio'] * producto['detalle'][0]['cantidad'])
            if producto['nombreProducto'] in productos:
                productos[producto['nombreProducto']]['detalle'][0]['cantidad'] += producto['detalle'][0]['cantidad']
            else:
                productos[producto['nombreProducto']] = producto
            productos = json.dumps(productos)
            carrito.productos = productos
            carrito.valor_compra = valor_total
            carrito.estado = 'en espera'
            carrito.actualizar()            
            
            return redirect(url_for('sell.home'))
    return render_template('sell/agregar_producto.html')

@sell.route('/compra/', methods=['GET','POST'])
def agregar_a_carrito():
    form = FormAgregarProducto()
    if form.validate_on_submit():
        nombre_producto = form.nombreProducto.data
        precio = form.precio.data
        cantidad = form.cantidad.data

        if not current_user.is_anonymous():
            lista_productos = 'lista_productos_' + str(current_user.get_id()) + '.xlsx'
            if path.exists(lista_productos):
                libroxl = load_workbook(lista_productos)
                #aqui se trabajara si existe el listado de productos del cliente
            else:
                #aqui se creara el archivo en caso de no existir
                libroxl= Workbook()
                hoja = libroxl.active

                libroxl.create_sheet('productos a comprar de s%'.%(current_user.email))
                hoja.append('nombre_de_producto','cantidad','precio_unitario','valor_total')
                hoja.append(nombre_producto,precio,cantidad,(precio * cantidad))

                libro.save(lista_productos) 

    return render_template('sell/agregar_producto.html', form=form)
