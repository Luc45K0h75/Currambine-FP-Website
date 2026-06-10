from flask import render_template
from app.models import Profile, DoctorType
from . import team
 
 
@team.route('/team')
def team_page():
    categories = DoctorType.query.order_by(DoctorType.type_id).all()
    return render_template('team.html', categories=categories)