from flask import Blueprint

sell = Blueprint('sell',__name__,template_folder='templates')

from . import route
