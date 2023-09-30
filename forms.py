from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    email = StringField('email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators =[DataRequired()])
    submit_button = SubmitField()
