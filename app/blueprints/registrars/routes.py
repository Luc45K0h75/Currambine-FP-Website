from flask import render_template, flash, redirect, url_for
from . import registrars
from app import limiter, mail
from .forms import RegistrarsApplicationForm
from flask_mail import Message
import os

@registrars.route('/registrars', methods=['GET', 'POST'])
@limiter.limit("10 per minute")
def registrars_page():
    form = RegistrarsApplicationForm()

    if form.validate_on_submit():
        msg = Message(
            subject=f'GP Training Application — {form.name.data}',
            recipients=[os.environ.get('MAIL_RECEIVER')],
            reply_to=form.email.data,
            body=f'''
New GP Registrar Application

Name: {form.name.data}
Email: {form.email.data}
Phone: {form.phone.data}
Preferred Term: {form.term.data}
Training Level: {form.training_level.data}

About:
{form.about.data or 'Not provided'}

Please reply to this email to contact the applicant.
Please ask them to send their CV to {os.environ.get('MAIL_RECEIVER')}
            '''
        )
        mail.send(msg)
        flash('Your application has been submitted successfully. We will be in touch soon.', 'success')
        return redirect(url_for('registrars.registrars_page'))

    return render_template('registrars.html', form=form)