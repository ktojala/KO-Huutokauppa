from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Kayttäjätunnus", [validators.Length(min=3)])
    password = PasswordField("Salasana")
  
    class Meta:
        csrf = False

class RegForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=3,max=144)])
    email = StringField("Email-osoite", [validators.Length(min=5,max=144)])
    username = StringField("Kayttäjätunnus", [validators.Length(min=3,max=144)])
    password = PasswordField("Salasana (vähintään 5 merkkiä)", [validators.Length(min=5, max=144)])
  
    class Meta:
        csrf = False

