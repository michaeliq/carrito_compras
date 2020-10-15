from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////storage/7091-1C0C/Android/data/com.termux/files/proyectos/carrito_de_compras/ADV.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

def create_app():

    from .sell import sell 
    app.register_blueprint(sell)

    from .admin import admin
    app.register_blueprint(admin)

    return app

