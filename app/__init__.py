from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
Bootstrap(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////storage/7091-1C0C/Android/data/com.termux/files/proyectos/carrito_de_compras/ADV.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'Ajh786ubkj_kjhk877.jh'

db = SQLAlchemy(app)
migration = Migrate(app,db)
login_manager = LoginManager(app)


def create_app():

    from .sell import sell 
    app.register_blueprint(sell)

    from .admin import admin
    app.register_blueprint(admin)

    from .auth import auth
    app.register_blueprint(auth)

    login_manager.login_view = "auth.login"

    return app

