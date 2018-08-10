from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, IntegerField, validators

class TuoteryhmaForm(FlaskForm):
    name = StringField("Tuoteryhmä:", [validators.Length(min=3)])
    done = BooleanField("Muuta") 

    class Meta:
        csrf = False

class MyytavaForm(FlaskForm):
    name = StringField("Nimike myytävälle:", [validators.Length(min=3)])
#    tuotetietoa = StringField("Tuotetietoa:", [validators.Length(max=144)])
    aloitushinta = IntegerField("Aloitushinta (tasaluku euroina)", [validators.NumberRange(min=1)])

#    done = BooleanField("Dani") 

    class Meta:
        csrf = False

