from application import db
from application.models import Base
  
class Tarjous(Base):

    __tablename__ = "tarjous"

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    myytava_id = db.Column(db.Integer, db.ForeignKey('myytava.id'), nullable=False)    
    tarjoussumma = db.Column(db.Integer)

    def __init__(self, asiakasid,myytavaid,summa):
        self.account_id = asiakasid
        self.myytava_id = myytavaid
        self.tarjoussumma = summa

