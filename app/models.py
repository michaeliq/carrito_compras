from app import db
from app import login_manager
from flask_login import UserMixin

class User(db.Model, UserMixin):

    __tablename__= 'usuarios'

    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(400),nullable=False)
    carrito_personal = db.relationship('Venta',backref='productos_a_comprar')

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @staticmethod
    def save(ref):
        db.session.add(ref)
        db.session.commit()

class Producto(db.Model):

    __tablename__="productos"

    
    id = db.Column(db.Integer, primary_key=True)
    producto = db.Column(db.String(35), unique=True, nullable=False)
    precio = db.Column(db.Float, nullable=False)
    descripcion = db.Column(db.String(100))
    img_pro = db.Column(db.String(100),default="")

    def __repr__(self):
        return '<Producto: %r>' % self.producto

    def save(self):
        db.session.add(self)
        db.session.commit()


    def values(self):
        return [self.id,self.producto,self.precio,self.descripcion,self.img_pro]


    def update_prod(self,n_nombre,n_precio,n_descripcion,image):
        self.producto = n_nombre or self.producto
        self.precio = n_precio or self.precio
        self.descripcion = n_descripcion or self.descripcion
        self.img_pro = image or self.img_pro

        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Carrito(db.Model):

    __tablename__='carrito'
    
    id_carrito = db.Column(db.Integer,primary_key=True)
    estado = db.Column(db.String,nullable=False)
    valor_compra = db.Column(db.Float,nullable=False)
    productos = db.Column(db.Float,nullable=False)
    id_cliente = db.Column(db.Integer,db.ForeignKey('usuarios.id'))

    def actuaizar(self):
        db.session.commit()

