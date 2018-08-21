
from flask_wtf import FlaskForm
from wtforms import IntegerField, validators

class TarjousForm(FlaskForm):
    tarjoussumma = IntegerField("Tarjoukseni (tasaluku euroina)", [validators.NumberRange(min=1, message="Tarjouksen oltava suurempi kuin edellinen tarjous")])

    class Meta:
        csrf = False
