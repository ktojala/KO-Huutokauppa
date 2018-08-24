
from flask import Flask
app = Flask(__name__)

# tietokantavaihtoehdot ja ORM
from flask_sqlalchemy import SQLAlchemy
import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:

# /// kertoo, että tiedosto sijaitsee tämän sovelluksen tiedostojen kanssa samassa paikassa
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///huutokauppa.db"
    app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)

# Kirjautumistoiminnallisuus

from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.setup_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Toiminto edellyttää kirjautumista "

# Rooli kirjautuessa

from functools import wraps
from application.auth.models import Rooli

def login_required(rooli="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            
            unauthorized = False

            if rooli != "ANY":
                unauthorized = True

#                for user_role in current_user.roles():
            for user_role in Rooli.anna_kayttajan_roolit(current_user.id):
                if user_role == rooli:
                    unauthorized = False
                    break

            if unauthorized:
                return login_manager.unauthorized()
            
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

# Sovelluksen toiminnallisuusluokat

from application import views

from application.tuoteryhma import models
from application.tuoteryhma import views

from application.myytava import models
from application.myytava import views

from application.auth import models
from application.auth import views

from application.tarjous import models
from application.tarjous import views


from application.auth.models import Asiakas, AsiakasRooli

@login_manager.user_loader
def load_user(user_id):
    return Asiakas.query.get(user_id)

# luodaan taulut tietokantaan tarvittaessa
try:
    db.create_all()

# luodaan pari perusasiakasta, jos niitä ei vielä ole
    asiakkaat = []
    try:
        asiat = Asiakas.query.all()
        for asia in asiat:
            if asia.name == 'admin':
                asiakkaat.append(asia.name)
        if asiakkaat == []:
            admin = Asiakas("admin","a@sti","admin","kadmin")
            testaaja = Asiakas("testaaja","t@sti","testi","kesti")

            admin_rooli = Rooli("ADMIN")
            asiakas_rooli = Rooli("ASIAKAS")
            vieras_rooli = Rooli("ANY")

            db.session.add_all((admin,testaaja,admin_rooli,asiakas_rooli,vieras_rooli))
            db.session.commit()

            ar1=AsiakasRooli()
            ar1.account_id = admin.id
            ar1.rooli_id = admin_rooli.id

            ar2=AsiakasRooli()
            ar2.account_id = testaaja.id
            ar2.rooli_id = asiakas_rooli.id

            db.session.add_all((ar1,ar2))
            db.session.commit()

    except:
        pass
except:
    pass


