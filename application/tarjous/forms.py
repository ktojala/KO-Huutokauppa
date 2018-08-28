
from flask_wtf import FlaskForm
from wtforms import IntegerField, validators

class TarjousForm(FlaskForm):
    tarjoussumma = IntegerField("Tarjoukseni: ", [validators.NumberRange(min=0,message="tasaluku euroina")])

    class Meta:
        csrf = False
