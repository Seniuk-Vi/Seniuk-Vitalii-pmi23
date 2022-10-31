from ..Model.CreditCard import CreditCard
from ..app import db
from ..Validator.Validator import Validator

class Card(CreditCard, db.Model):
    __tablename__ = 'creditcards'
    id = db.Column(db.Integer, primary_key=True)
    bank = db.Column(db.String(255), nullable=False)
    card_number = db.Column(db.String(19), unique=True, nullable=False)
    date_of_issue = db.Column(db.DateTime(), nullable=False)
    date_of_expire = db.Column(db.DateTime(), nullable=False)
    cvc = db.Column(db.Integer(), nullable=False)
    owner_name = db.Column(db.String(50), nullable=False)

    def __init__(self, bank, card_number, date_of_issue, date_of_expire, cvc, owner_name):

       # super().__init__(**{'bank': bank, 'card_number': card_number, 'date_of_issue': date_of_issue,
             #               'date_of_expire': date_of_expire, 'cvc': cvc, 'owner_name': owner_name})
        super(Card, self).__init__(**{'bank': bank, 'card_number': card_number, 'date_of_issue': date_of_issue,
                            'date_of_expire': date_of_expire, 'cvc': cvc, 'owner_name': owner_name})
    def to_json(self):
        return {
            'id': self.id,
            'bank': self.bank,
            'card_number': self.card_number,
            'date_of_issue': self.date_of_issue,
            'date_of_expire': self.date_of_expire,
            'owner_name': self.owner_name,
            'cvc': self.cvc
        }
