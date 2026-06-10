from flask import render_template, flash, redirect, url_for
from app.models import Profile, DoctorType
from . import fellows
from app import limiter, mail
from .forms import FellowsApplicationForm
from flask_mail import Message
import os

@fellows.route('/fellows', methods=['GET', 'POST'])
@limiter.limit("10 per minute") #DDOS protection: limit to 10 requests per minute
def fellows_page():
    form = FellowsApplicationForm()

    # CSRF protection and form handling
    if form.validate_on_submit():
        msg = Message(
            subject="New Fellow Application",
            recipients=[os.getenv('MAIL_RECEIVER')],
            body=f'''
New Fellows Application for Currambine Family Practice

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
                      
        flash('Your application has been submitted successfully. We will be in touch soon.', 'success')
        return redirect(url_for('fellows.fellows_page'))

    return render_template('fellows.html', form=form)