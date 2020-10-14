from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

def create_app():

    from .sell import sell
    app.register_blueprint(sell)

    from .admin import admin
    app.register_blueprint(admin)

    return app

