from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, IntegerField, validators

class MyytavaForm(FlaskForm):
    name = StringField("Nimike myytävälle:", [validators.Length(min=3)])
#    tuotetietoa = StringField("Tuotetietoa:", [validators.Length(max=144)])
    aloitushinta = IntegerField("Aloitushinta (tasaluku euroina)", [validators.NumberRange(min=1)])

#    done = BooleanField("Dani") 

    class Meta:
        csrf = False