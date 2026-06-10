from flask import render_template, flash
from app.models import Profile, DoctorType
from . import fellows
from app import limiter, mail
from .forms import FellowsApplicationForm
from flask_mail import Message
import os

@limiter.limit("10 per minute") #DDOS protection: limit to 10 requests per minute
@fellows.route('/fellows')
def fellows():
    form = FellowsApplicationForm()

    # CSRF protection and form handling
    if form.validate_on_submit():
        msg = Message(
            subject="New Fellow Application",
            recipients=[os.getenv('MAIL_RECEIVER')],
            body=f'''
New Fellows Application

Name: {form.name.data}
Email: {form.email.data}
Phone: {form.phone.data}
FRACGP Fellow: {'Yes' if form.is_fracgp.data else 'No'}

About:
{form.about.data or 'Not provided'}

Please reply to this email to contact the applicant.
Please ask them to send their CV to {os.environ.get('MAIL_RECEIVER')}
            '''
        )
        mail.send(msg)
                      
        return render_template('fellows.html', form=form)

    return render_template('fellows.html')