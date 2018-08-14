
# Tuodaan Flask käyttöön
from flask import Flask
app = Flask(__name__)

# tietokanta
from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:

# /// kertoo, tiedosto sijaitsee tämän sovelluksen tiedostojen kanssa samassa paikassa
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///huutokauppa.db"
    app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)


# oman sovelluksen toiminnallisuudet
from application import views

from application.tasks import models
from application.tasks import views

from application.myytava import models
from application.myytava import views

from application.auth import models
from application.auth import views


# kirjautuminen
from application.auth.models import Asiakas
from os import urandom
app.config["SECRET_KEY"] = urandom(32)


from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Toiminto edellyttää rekisteröitymista tai sisäänkirjautumista "


@login_manager.user_loader
def load_user(user_id):
    return Asiakas.query.get(user_id)

# luodaan taulut tietokantaan tarvittaessa
try:
    db.create_all()
except:
    pass

