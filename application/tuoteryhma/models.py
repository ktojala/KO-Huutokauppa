
from application import db
from application.models import Base

from sqlalchemy.sql import text
  
class Tuoteryhma(Base):

    __tablename__ = "tuoteryhma"

    name = db.Column(db.String(144), unique=True, nullable=False)
#    done = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name):
        self.name = name
#        self.done = False


#    @staticmethod
#    def etsi_tuoteryhman_myytavat():
#        komen = text("SELECT * FROM myytava")
#        res = db.engine.execute(komen)
#        response =[]
#        for row in res:
#            response.append
        
    @staticmethod
    def montako_tuotetta_ryhmassa(tr):
#        stmt = text("SELECT COUNT(name) FROM myytava WHERE :id=tr.id")
        stmt = text("SELECT COUNT(id) FROM myytava ")
        res = db.engine.execute(stmt).scalar()
        return res

