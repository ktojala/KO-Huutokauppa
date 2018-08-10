from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, IntegerField, validators

class TuoteryhmaForm(FlaskForm):
    name = StringField("Tuoteryhmä:", [validators.Length(min=3)])
    done = BooleanField("Dani") 

    class Meta:
        csrf = False

class MyytavaForm(FlaskForm):
    name = StringField("Nimike myytävälle:", [validators.Length(min=3)])
#    seloste = StringField("Tuoteseloste:", [validators.Length(min=1, max=144)])
#    hinta = IntegerField("Tarjous:", [validators.NumberRange(min=1)])
    done = BooleanField("Dani") 

    class Meta:
        csrf = False
