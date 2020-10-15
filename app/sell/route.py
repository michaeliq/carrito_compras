from flask import render_template, redirect, url_for

from . import sell
from app.models import Producto

@sell.route('/home/')
def home():
    productos = Producto.query.all()
    return render_template('sell/home_page.html',productos = productos)


