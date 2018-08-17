
from application import db
from application.models import Base

class Asiakas(Base):

# Ei suomenneta account-sanaa
    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    email = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    tuoteryhma = db.relationship("Tuoteryhma", backref='account', lazy=True)
    myytava = db.relationship("Myytava", backref='account', lazy=True)

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
