from app import db
from app import login_manager
from flask_login import UserMixin

class User(db.Model, UserMixin):

    __tablename__= 'usuarios'

    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(400),nullable=False)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)


class Producto(db.Model):

    __tablename__="productos"

    id = db.Column(db.Integer, primary_key=True)
    producto = db.Column(db.String(35), unique=True, nullable=False)
    precio = db.Column(db.Float, nullable=False)
    descripcion = db.Column(db.String(100))

    def __repr__(self):
        return '<Producto: %r>' % self.producto

    def save(self):
        db.session.add(self)
        db.session.commit()

    def values(self):
        return [self.id,self.producto,self.precio,self.descripcion]

    def update_prod(self,n_nombre,n_precio,n_descripcion):
        self.producto = n_nombre or self.producto
        self.precio = n_precio or self.precio
        self.descripcion = n_descripcion or self.descripcion

        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
'''
class Venta(db.Model):

    __tablename__='ventas'

    def __init__(self,valor_compra,productos):
        self.valor_compra = valor_compra
        self.productos = prouctos
        self.num_factura = 0 #añadir qr

    @staticmethod
    def obtener_factura(qr):
        return Venta.query.filter_by(num_factura = qr).first()

    def fijar_numero_fact(self):
        pass
'''
