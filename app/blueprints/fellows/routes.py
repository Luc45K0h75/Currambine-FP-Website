from flask import render_template, flash
from app.models import Profile, DoctorType
from . import fellows
from app import limiter
from .forms import FellowsApplicationForm

@limiter.limit("10 per minute") #DDOS protection: limit to 10 requests per minute
@fellows.route('/fellows')
def fellows():
    form = FellowsApplicationForm()

    # CSRF protection and form handling
    if form.validate_on_submit():
        flash('Application submitted successfully!', 'success')
        return render_template('fellows.html', form=form)

    return render_template('fellows.html')