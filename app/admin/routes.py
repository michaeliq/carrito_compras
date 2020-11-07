from flask import render_template, url_for, redirect, request
from flask_login import login_required
from openpyxl import Workbook
from os import path

from app.models import Producto
from .forms import FormCrearProducto, FormModificar
from app.obtener_img import fijar_img

from . import admin

@admin.route('/admin/front/')
@login_required
def front():
    productos = Producto.query.all()
    print(productos)
    return render_template('admin/front.html',prod= productos)

@admin.route('/admin/crear/',methods=['POST','GET'])
@login_required
def crear():
    form = FormCrearProducto()
    if form.validate_on_submit():
        nuevo_p = Producto(producto=form.nombreProducto.data, precio=form.precio.data,descripcion=form.descripcion.data,img_pro=fijar_img(form.nombreProducto.data))
        Producto.save(nuevo_p)
        print(f'se ha añadido {nuevo_p} a el inventario')
        return redirect(url_for('sell.home'))
    return render_template('admin/crear_prod.html',forms=form)

@admin.route('/admin/modificar/<_id>/',methods=['POST','GET'])
@login_required
def modificar_producto(_id=None):
    form = FormModificar() 
    if form.validate_on_submit():
        prod = Producto.query.get(request.form["id"])
        viejo_n = prod.producto
        nomb = form.nombreProducto.data
        precio = form.precio.data
        descp = form.descripcion.data
        image = fijar_img(nomb)

        prod.update_prod(nomb,precio,descp,image)
        print(f'el producto {viejo_n} ha sido actualizado')
        return redirect(url_for('admin.front'))
    elif request.method == 'GET' and _id is not None:
        values = Producto.query.get(_id)
        return render_template('admin/actualizar_prod.html',forms=form,values=values)

    else:
        return redirect(url_for('sell.home'))


@admin.route('/admin/delete/<id>/',methods=['GET'])
@login_required
def delete(id):
    if request.method == 'GET':
        prod = Producto.query.get(id)
        prod.delete()
        print('Producto eliminado')
        return redirect(url_for('admin.front'))

@admin.route('/admin/reports/')
@login_required
def report():
    return render_template('admin/reports.html')

@admin.route('/admin/report_product/<nomb_p>/')
@login_required
def report_product(nomb_p):

    prod = Producto.query.filter_by(producto=nomb_p).first()
    libro = Workbook()
    hoja = libro.active
    contador_replicas = 1
    nombre_lib = f'reporte_{prod.producto}_'

    while path.exists(nombre_lib + str(contador_replicas) + '.xlsx') == True:
        contador_replicas += 1
        
    libro.create_sheet(nombre_lib + str(contador_replicas))
    hoja.append(('Nombre de Producto','Precio','Cantidad en Stock','Unidades Vendidas','Valor de Ventas'))

    lista_prod = prod.values()
    hoja.append(lista_prod)

    libro.save(nombre_lib + str(contador_replicas) + '.xlsx')

    return redirect(url_for('admin.front'))
        
        

@admin.route('/admin/control_panel/')
@login_required
def control_panel():
    pass


