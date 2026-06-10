from flask import Blueprint

team = Blueprint('team', __name__, template_folder='templates')

from . import routes