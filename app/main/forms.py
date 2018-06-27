from flask_wtf import FlaskForm
from wtforms.validators import Required
from wtforms import SubmitField, TextAreaField

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')
