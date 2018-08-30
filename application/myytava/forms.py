
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, IntegerField, validators

class MyytavaForm(FlaskForm):
    name = StringField("Nimike myytävälle:", [validators.Length(min=3, max=40, message="Pituus 3-40 merkkiä")])
    tuotetietoa = StringField("Tuotetietoa:", [validators.Length(min=10, max=144, message="Pituus 10-144 merkkiä")])
    aloitushinta = IntegerField("Aloitushinta (tasaluku euroina) ", [validators.NumberRange(min=1, message="Vähintään 1 (eur)")])
    tarjousaikaa = IntegerField("Tarjousaikaa jäljellä (3-28 vrk)", [validators.NumberRange(min=3, max=28, message="Oltava 3-28 (vrk)")])
    class Meta:
        csrf = False


