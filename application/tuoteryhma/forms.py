from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, IntegerField, validators

class TuoteryhmaForm(FlaskForm):
    name = StringField("Tuoteryhmä:", [validators.Length(min=3)])
    done = BooleanField("Muuta") 

    class Meta:
        csrf = False


