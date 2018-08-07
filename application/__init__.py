
# Tuodaan Flask käyttöön
from flask import Flask
app = Flask(__name__)

# tietokanta
from flask_sqlalchemy import SQLAlchemy
# Kolme vinoviivaa kertoo, tiedosto sijaitsee tämän sovelluksen 
# tiedostojen kanssa samassa paikassa
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///huutokauppa.db"
app.config["SQLALCHEMY_ECHO"] = True
# Pyydettiin SQLAlchemyä tulostamaan kaikki SQL-kyselyt

# Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)

# oman sovelluksen toiminnallisuudet
from application import views

from application.tasks import models
from application.tasks import views

from application.auth import models
from application.auth import views

# kirjautuminen
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# luodaan taulut tietokantaan tarvittaessa
db.create_all()
