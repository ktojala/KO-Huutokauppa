
from application import db
from application.models import Base
from application.myytava.models import Myytava
from application.tuoteryhma.models import Tuoteryhma
from application.tarjous.models import Tarjous
from sqlalchemy.sql import text

import traceback

class Asiakas(Base):

# Ei suomenneta account-sanaa
    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    email = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    tuoteryhma = db.relationship("Tuoteryhma", backref='account', lazy=True)
    myytava = db.relationship("Myytava", backref='account', lazy=True)
    asiakas_rooli = db.relationship("AsiakasRooli", backref='account', lazy=True)

    def __init__(self, name,email,username,password):
        self.name = name
        self.email = email
        self.username = username
        self.password = password

  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def get_name(self,id):
        return self.name

#    def admin_on_olemassa(self):
#        return Asiakas.query.join(
#        stmt = text("SELECT account.name FROM account WHERE account.name = 'admin';")
#        res = db.engine.execute(stmt)
#        nimet = []
#        for nimi in nimet:
#            if nimi == 'admin':
#                return True
#        return False


    def omaa_roolin(self, rooli_nimike):
        return True
#        roolit = self.roolit()
#        for rooli in roolit:
#            if rooli.nimi == rooli_nimike:
#                return True
#        return False
#

    def roolit(self):
        return Rooli.query.join(Rooli.user_roles).filter_by(account_id=self.id).all()
#        return ["ADMIN"]



class Rooli(Base):
    __tablename__ = "rooli"
    name = db.Column(db.String(50), nullable=False)
    user_roles = db.relationship("AsiakasRooli", backref="rooli", lazy = True)

    def __init__(self,name):
        self.name = name

    @staticmethod
    def anna_kayttajan_roolit(account_id):
        stmt = text("SELECT DISTINCT Rooli.name FROM Rooli JOIN AsiakasRooli ON"
                    " Rooli.id = AsiakasRooli.rooli_id WHERE AsiakasRooli.account_id = "
                    "account_id").params(account_id=account_id)

        res = db.engine.execute(stmt)
        roolit = []
        for rivi in res:
            roolit.append(rivi[0])
        return roolit
     


class AsiakasRooli(Base):
    __tablename__ = "asiakasrooli"

    account_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)
    rooli_id   = db.Column(db.Integer, db.ForeignKey("rooli.id"), nullable=False)








