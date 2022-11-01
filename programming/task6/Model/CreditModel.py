from Seniuk.programming.task6.Model.CreditCard import CreditCard
from Seniuk.programming.task6.app import db
from Seniuk.programming.task6.Validator.Validator import Validator
from Seniuk.programming.task6.Enums.Banks import *
from Seniuk.programming.task6.Validator.CreditCardRegex import *
from sqlalchemy.orm import validates
from datetime import datetime
from copy import deepcopy


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
        print("constrictor")
        # super().__init__(**{'bank': bank, 'card_number': card_number, 'date_of_issue': date_of_issue,
        #               'date_of_expire': date_of_expire, 'cvc': cvc, 'owner_name': owner_name})
        super(Card, self).__init__(**{'bank': bank, 'card_number': card_number, 'date_of_issue': date_of_issue,
                                      'date_of_expire': date_of_expire, 'cvc': cvc, 'owner_name': owner_name})

    @validates('bank')
    def validate_bank(self, key, bank):
        if not Validator.is_in_map([e.value for e in Banks], bank):
            raise AttributeError("Bank isn't correct!!!")
        return bank

    @validates('card_number')
    def validate_card_number(self, key, card_number):
        if not Validator.validate_with_regex(CreditCardRegex.card_regex, card_number):
            raise AttributeError("Card number isn't correct!!!")
        return card_number

    @validates('cvc')
    def validate_cvc(self, key, cvc):
        if not Validator.validate_with_regex(CreditCardRegex.cvc_regex, str(cvc)):
            raise AttributeError("Cvc isn't correct!!!")
        return cvc

    @validates('owner_name')
    def validate_owner_name(self, key, owner_name):
        if not Validator.validate_with_regex(CreditCardRegex.owner_name_regex, owner_name):
            raise AttributeError("owner name isn't correct!!!")
        return owner_name

    @validates('date_of_issue', 'date_of_expire')
    def validate_dates(self, key, field):
        date_format = "%Y-%m-%d"
        print(field)
        try:
            start = deepcopy(field)
            date_format = "%Y-%m-%d"
            start = datetime.strptime(start, date_format)
        except Exception:
            raise AttributeError(f"Field must be formatted like {date_format}")
        print(f"is: {self.date_of_issue}")
        print(f"ex: {self.date_of_expire}")
        if key == 'date_of_expire' and self.date_of_issue is not None and start < self.date_of_issue or \
                key == 'date_of_issue' and self.date_of_expire is not None and self.date_of_expire < start:
            raise AttributeError("The date_of_expire field must be " \
                                 "greater-or-equal than the date_of_issue field")
        return start

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
