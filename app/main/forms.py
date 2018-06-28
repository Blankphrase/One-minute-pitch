from flask_wtf import FlaskForm
from wtforms.validators import Required,Email
from wtforms import SubmitField, TextAreaField, StringField,ValidationError
from ..models import User


class ReviewForm(FlaskForm):

    username = StringField('Username', validators=[Required()])
    review = TextAreaField('Pitch review', validators=[Required()])
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    username = StringField('Username', validators = [Required()])
    post = TextAreaField('Pitch', validators = [Required()])
    submit = SubmitField('Submit')