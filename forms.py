from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, IntegerField, Form, RadioField, ValidationError, SubmitField, validators


class LoginForm(FlaskForm):
    username = StringField('username', validators=[validators.Length(min=5, max=25)])
    password = StringField('password', validators=[validators.Length(min=5, max=25)])
    submit = SubmitField("Submit")
    
    
class RegisterForm(FlaskForm):
    username = StringField('username', validators=[validators.Length(min=5, max=25)])
    password = StringField('password', validators=[validators.Length(min=5, max=25)])
    submit = SubmitField("Submit")
    
class AddGame(FlaskForm):
    title = StringField('title',validators=[validators.Length(max=75)])
    genre = StringField('title',validators=[validators.Length(max=250)])
    vg_console = SelectField('genre')
    release_yr = IntegerField('Year Released')
    play_yr =IntegerField ('Year Played')
    description = StringField('Description', validators=[validators.Length(max=250)])
    rating = IntegerField('Rating', validators=[validators.NumberRange(min=0, max=10)])
    submit = SubmitField("Submit")