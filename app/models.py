from flask_sqlalchemy import SQLAlchemy
from .app import db

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////ADV.sql'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producto = db.Column(db.String(35), unique=True, nullable=False)
    precio = db.Column(db.Float, nullable=False)
    descripcion = db.Column(db.String(100))

    def __repr__(self):
        return '<Producto: %r>' % self.producto
