from flask import Blueprint

fellows = Blueprint('fellows', __name__, template_folder='templates')

from . import routes