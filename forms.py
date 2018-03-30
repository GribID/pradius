from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators


class LoginForm(FlaskForm):
    name = StringField('name', [validators.Length(min=4, max=20)])
    pwd = PasswordField('pass', [validators.Length(min=4, max=20)])

