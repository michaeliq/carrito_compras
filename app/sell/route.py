from flask import render_template, redirect, url_for

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
                'cantidad':form.cantidad.data
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
