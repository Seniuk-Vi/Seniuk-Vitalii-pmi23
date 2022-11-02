import re
from ..Enums.Banks import Banks
# from CreditCardRegex import *
from datetime import datetime

JSON = "json"
class CreditCardRegex:
    owner_name_regex = "^[a-zA-z ,.'-]+$"
    id_regex = "\\d{1,15}"
    card_regex = "(\\d{4}) (\\d{4}) (\\d{4}) (\\d{4})"
    cvc_regex = "\\d{3}"


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
                date_format = "%Y-%m-%d"
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
                date_format = "%Y-%m-%d"
                start = datetime.strptime(val, date_format)
                if start <= datetime.now():
                    raise AttributeError()
            except Exception:
                raise AttributeError("Date can't be in past!!!")
            return func(self, val)

        return validateFuture

    @staticmethod
    def decoratorJsonFile(func):
        def validateJsonFile(self, filename):
            if not filename.endswith(JSON):
                raise AttributeError("File should end with ." + JSON)
            return func(self, filename)

        return validateJsonFile

    @staticmethod
    def is_in_map(map, value):
        return value in map

    @staticmethod
    def validateFileName(filename, end=".txt"):
        if not filename.endswith(end):
            raise AttributeError("File should end with ." + end)
        return filename
