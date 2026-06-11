from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, Length, Optional

class RegistrarsApplicationForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired(), Length(max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[Length(max=20)])
    term = SelectField('Preferred Term', choices=[
        ('', 'Select term'),
        ('term_1', 'Term 1'),
        ('term_2', 'Term 2'),
        ('term_3', 'Term 3'),
        ('term_4', 'Term 4'),
    ], validators=[DataRequired()])
    training_level = SelectField('Training Level', choices=[
        ('', 'Select level'),
        ('registrar', 'GP Registrar'),
        ('advanced', 'Advanced Training'),
    ], validators=[DataRequired()])
    about = TextAreaField('Tell us about yourself', validators=[Optional(), Length(max=3000)])