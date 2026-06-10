from flask import Blueprint, render_template
 
main = Blueprint('main', __name__)
 
 
@main.route('/')
def index():
    return render_template('index.html')
 
 
@main.route('/about')
def about():
    return render_template('about.html')
 
 
@main.route('/services')
def services():
    return render_template('services.html')
 
 
@main.route('/team')
def team():
    from app.models import Profile, DoctorType
    categories = DoctorType.query.order_by(DoctorType.type_id).all()
    return render_template('team.html', categories=categories)
 
 
@main.route('/contact')
def contact():
    return render_template('contact.html')
 
 
@main.route('/appointments')
def appointments():
    return render_template('appointments.html')


@main.route('/fellows')
def fellows():
    return render_template('fellows.html')

@main.route('/registrars')
def registrars():
    return render_template('registrars.html')