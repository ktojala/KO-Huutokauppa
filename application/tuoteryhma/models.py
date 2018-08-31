
from application import db
from application.models import Base
from application.myytava.models import Myytava
from sqlalchemy.sql import text
  
class Tuoteryhma(Base):

    __tablename__ = "tuoteryhma"

    name = db.Column(db.String(144), unique=True, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    myytavat = db.relationship("Myytava", backref="tuoteryhma", lazy=True)

    def __init__(self, name):
        self.name = name


    @staticmethod
    def montako_tuotetta_ryhmassa(tr):
        return db.session.query(Myytava).filter_by(tuoteryhma_id=tr.id).count()
