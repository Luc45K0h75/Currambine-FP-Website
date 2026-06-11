from flask import Blueprint

registrars = Blueprint('registrars', __name__, template_folder='templates')

from . import routes