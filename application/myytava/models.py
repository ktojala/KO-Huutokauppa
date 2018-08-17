from application import db
from application.models import Base
  
class Myytava(Base):

    __tablename__ = "myytava"

    name = db.Column(db.String(144), nullable=False)
    aloitushinta = db.Column(db.Integer, nullable=False)
    tarjoushinta = db.Column(db.Integer, nullable=False)
#    tuotetietoa = db.Column(db.String(144), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    tuoteryhma_id = db.Column(db.Integer, db.ForeignKey('tuoteryhma.id'), nullable=False)

    def __init__(self, name,tuoteryhma):
        self.name = name
        self.aloitushinta = 1
        self.tarjoushinta = 1
        self.tuoteryhma_id = tuoteryhma
