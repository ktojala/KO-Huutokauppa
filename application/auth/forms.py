from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Kayttäjätunnus", [validators.Length(min=3)])
    password = PasswordField("Salasana")
  
    class Meta:
        csrf = False

