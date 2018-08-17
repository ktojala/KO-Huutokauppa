from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, IntegerField, validators

class TuoteryhmaForm(FlaskForm):
    name = StringField("Tuoteryhmä:", [validators.Length(min=3,max=40, message="Pituus 3-40 merkkiä")])
#    done = BooleanField("Muuta") 

    class Meta:
        csrf = False


