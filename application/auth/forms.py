from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Kayttäjätunnus", [validators.Length(min=3)])
    password = PasswordField("Salasana", [validators.Length(min=5, max=40, message="Salasana?")])
  
    class Meta:
        csrf = False

class RegForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=3,max=60, message="Nimen pituus 3-60 merkkiä")])
    email = StringField("Email-osoite", [validators.Length(min=5,max=60, message="Email-osoitteen pituus 5-60 merkkiä)")])
    username = StringField("Kayttäjätunnus", [validators.Length(min=3,max=40, message="Tunnuksen pituus 3-40 merkkiä")])
    password = PasswordField("Salasana (vähintään 5 merkkiä)", [validators.Length(min=5, max=40, message="Salasanan pituus 5-40 merkkiä")])
  
    class Meta:
        csrf = False

