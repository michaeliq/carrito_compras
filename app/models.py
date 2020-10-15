from app import db

class Producto(db.Model):

    __tablename__="productos"

    id = db.Column(db.Integer, primary_key=True)
    producto = db.Column(db.String(35), unique=True, nullable=False)
    precio = db.Column(db.Float, nullable=False)
    descripcion = db.Column(db.String(100))

    def __repr__(self):
        return '<Producto: %r>' % self.producto
