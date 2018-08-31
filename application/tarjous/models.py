from application import db
from application.models import Base
from application.myytava.models import Myytava

from sqlalchemy.sql import text
  
class Tarjous(Base):

    __tablename__ = "tarjous"

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    myytava_id = db.Column(db.Integer, db.ForeignKey('myytava.id'), nullable=False)    
    tarjoussumma = db.Column(db.Integer)

    def __init__(self, asiakasid,myytavaid,summa):
        self.account_id = asiakasid
        self.myytava_id = myytavaid
        self.tarjoussumma = summa


    @staticmethod
    def myytavan_nimi(m_id):
        stmt = text("SELECT myytava.name FROM myytava WHERE myytava.id = :idi").params(idi=m_id)
        res = db.engine.execute(stmt)
        response = []

        for nimi in res:
            response.append(nimi[0])

        return response

    @staticmethod
    def myytavan_tarjoukset_poista(myytava_id):

        stmt = text("DELETE FROM tarjous WHERE tarjous.myytava_id = :idi").params(idi=myytava_id)
        db.engine.execute(stmt)
        return


    @staticmethod
    def umpeutunut(m_id):
        stmt = text("SELECT myytava.tarjousaikaa FROM myytava WHERE myytava.id = :idi").params(idi=m_id)
        res = db.engine.execute(stmt).scalar()

        if res == 0:
            return True
        else:
            return False
