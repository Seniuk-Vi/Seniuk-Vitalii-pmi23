import re
from CreditCardRegex import *
from Banks import *
from datetime import datetime


class Validator:

    @staticmethod
    def validate_with_regex(regex, arg):
        boo = re.fullmatch(regex, str(arg)) is not None
        return boo

    @staticmethod
    def decoratorId(func):
        def validateId(self, val):
            if not Validator.validate_with_regex(CreditCardRegex.id_regex, val):
                raise AttributeError("Id isn't correct!!!")
            return func(self, val)

        return validateId

    @staticmethod
    def decoratorCvc(func):
        def validateCvc(self, val):
            if not Validator.validate_with_regex(CreditCardRegex.cvc_regex, val):
                raise AttributeError("Cvc isn't correct!!!")
            return func(self, val)

        return validateCvc

    @staticmethod
    def decoratorName(func):
        def validateName(self, val):
            if not Validator.validate_with_regex(CreditCardRegex.owner_name_regex, val):
                raise AttributeError("Name isn't correct!!!")
            return func(self, val)

        return validateName

    @staticmethod
    def decoratorBank(func):
        def validateBank(self, val):
            if not Validator.is_in_map([e.value for e in Banks], val):
                raise AttributeError("Bank isn't correct!!!")
            return func(self, val)

        return validateBank

    @staticmethod
    def decoratorCard(func):
        def validateCard(self, val):
            if not Validator.validate_with_regex(CreditCardRegex.card_regex, val):
                raise AttributeError("Card number isn't correct!!!")
            return func(self, val)

        return validateCard

    @staticmethod
    def decoratorDatePass(func):
        def validateDatePass(self, val):
            try:
                date_format = "%d/%m/%Y"
                start = datetime.strptime(val, date_format)
                if start >= datetime.now():
                    raise AttributeError()
            except Exception:
                raise AttributeError("Date can't be in future!!!")
            return func(self, val)

        return validateDatePass

    @staticmethod
    def decoratorDateFuture(func):
        def validateFuture(self, val):
            try:
                date_format = "%d/%m/%Y"
                start = datetime.strptime(val, date_format)
                if start <= datetime.now():
                    raise AttributeError()
            except Exception:
                raise AttributeError("Date can't be in past!!!")
            return func(self, val)

        return validateFuture

    @staticmethod
    def is_in_map(map, value):
        return value in map

    @staticmethod
    def validateFileName(filename, end=".txt"):
        if not filename.endswith(end):
            raise ValueError("File should end with ." + end)
        return filename
