
from application import db
from application.models import Base
  
class Tuoteryhma(Base):

    __tablename__ = "tuoteryhma"

    name = db.Column(db.String(144), nullable=False)
    done = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name):
        self.name = name
        self.done = False

#    @staticmethod
#    def etsi_tuoteryhman_myytavat():
#        komen = text("SELECT * FROM myytava")
#        res = db.engine.execute(komen)
#        response =[]
#        for row in res:
#            response.append
        

