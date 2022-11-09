from Seniuk.task8.app import db
from Seniuk.task8.app import app
from Seniuk.task8.Validator.Validator import Validator
from Seniuk.task8.Enums.Banks import *
from Seniuk.task8.Validator.CreditCardRegex import *
from sqlalchemy.orm import validates
from datetime import datetime
from copy import deepcopy
import jwt


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    email = db.Column(db.String(70), unique=True)
    password = db.Column(db.String(256))
    admin = db.Column(db.Boolean)
    # npassword = None

    @validates('name')
    def validate_name(self, key, name):
        if not Validator.validate_with_regex(CreditCardRegex.owner_name_regex, name):
            raise AttributeError("Name isn't correct!!!")
        return name

    @validates('surname')
    def validate_surname(self, key, surname):
        if not Validator.validate_with_regex(CreditCardRegex.owner_name_regex, surname):
            raise AttributeError("Surname isn't correct!!!")
        return surname

    @validates('email')
    def validate_email(self, key, email):
        print(email)
        if not Validator.validate_with_regex(CreditCardRegex.email_regex, email):
            raise AttributeError("Email isn't correct!!!")
        return email

    # @validates('npassword')
    # def validate_npassword(self, key, npassword):
    #     print(npassword)
    #     if not Validator.validate_with_regex(CreditCardRegex.password_regex, npassword) or len(
    #             npassword) < 8:
    #         raise AttributeError("Password is too weak (minimum 1 upper and minimum 1 lower and 8 characters)!!!")
    #     return npassword

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'email': self.email
        }
