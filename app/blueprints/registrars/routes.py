from flask import render_template
from . import registrars


@registrars.route('/registrars')
def registrars_page():
    return render_template('registrars.html')