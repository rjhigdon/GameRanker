from wtforms import Form, SelectField, StringField, IntegerField, RadioField, validators


class LoginForm():
    username = StringField('username', validators.Length(min=5, max=25))
    password = StringField('password', validators.Length(min=5, max=25))
    
    
class RegisterForm():
    username = StringField('username', validators.Length(min=5, max=25))
    password = StringField('password', validators.Length(min=5, max=25))
    
class AddGame():
    title = StringField('title', validators.Length(max=75))
    genre = StringField('title',validators.Length(max=250))
    vg_console = SelectField('genre')
    release_yr = IntegerField('Year Released')
    play_yr =IntegerField ('Year Played')
    description = StringField('Description', validators.Length(max=250))
    rating = IntegerField('Rating', validators.NumberRange(min=0, max=10))