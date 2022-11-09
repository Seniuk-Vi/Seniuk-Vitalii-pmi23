from Seniuk.task8.app import db
from Seniuk.task8.Validator.Validator import Validator
from Seniuk.task8.Enums.Banks import *
from Seniuk.task8.Validator.CreditCardRegex import *
from sqlalchemy.orm import validates
from datetime import datetime
from copy import deepcopy


class TokenBlackList(db.Model):
    __tablename__ = 'tokenblacklist'
    token = db.Column(db.String, primary_key=True, autoincrement=False)

    @validates('bank')
    def validate_bank(self, key, bank):
        if not Validator.is_in_map([e.value for e in Banks], bank):
            raise AttributeError("Bank isn't correct!!!")
        return bank


    def to_json(self):
        return {
            'token': self.token

        }
