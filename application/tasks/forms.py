from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class TaskForm(FlaskForm):
    name = StringField("Tuoteryhmä:", [validators.Length(min=2)])
    done = BooleanField("Dani") 

    class Meta:
        csrf = False

