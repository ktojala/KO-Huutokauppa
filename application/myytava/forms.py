
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, IntegerField, validators

class MyytavaForm(FlaskForm):
    name = StringField("Nimike myytävälle:", [validators.Length(min=3, max=40, message="Pituus 3-40 merkkiä")])
    tuotetietoa = StringField("Tuotetietoa:", [validators.Length(min=10, max=144, message="Pituus 10-144 merkkiä")])
    aloitushinta = IntegerField("Aloitushinta (tasaluku euroina)", [validators.NumberRange(min=1, message="Vähintään 1 (eur)")])
#    tarjoushinta = IntegerField("Korkein tarjous", [validators.NumberRange(min=1)])
#    tuoteryhma_id = IntegerField("Aloitushinta (tasaluku euroina)", [validators.NumberRange(min=1)])

    class Meta:
        csrf = False
