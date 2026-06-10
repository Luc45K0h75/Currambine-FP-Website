from flask import render_template
from app.models import Profile, DoctorType
from . import fellows

@fellows.route('/fellows')
def fellows():
    return render_template('fellows.html')