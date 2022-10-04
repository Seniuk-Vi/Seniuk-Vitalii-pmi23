import os

from Validator import *
from CreditCardRegex import *
from Banks import *

LINE_SEP = os.linesep


class CreditCard:
    def __init__(self, **array):
        for (key, value) in array.items():
            setattr(self, key, array.get(key, value))

    def __str__(self):
        result = ""
        for i in dir(self):
            if not i.startswith("__") and not i.startswith("_") and i != "input":
                result += i + ": " + str(getattr(self, i)) + "\n"
        return result

    def __repr__(self):
        result = ""
        for i in dir(self):
            if not i.startswith("__") and not i.startswith("_") and i != "input":
                result += i + ": " + str(getattr(self, i)) + ". "
        result += LINE_SEP
        return result

    def __eq__(self, other):
        print("equal")
        return self.id == other.id

    def __hash__(self):
        print("hash")
        return hash(self.id)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, val):
        if not Validator.validate_with_regex(CreditCardRegex.id_regex, val):
            raise AttributeError("ID isn't correct!!!")
        self._id = val

    @property
    def bank(self):
        return self._bank

    @bank.setter
    def bank(self, val):
        if not Validator.is_in_map([e.value for e in Banks], val):
            raise AttributeError("Bank isn't correct!!!")
        self._bank = val

    @property
    def card_number(self):
        return self._card_number

    @card_number.setter
    def card_number(self, val):
        if not Validator.validate_with_regex(CreditCardRegex.card_regex, val):
            raise AttributeError("Card number isn't correct!!!")
        self._card_number = val

    @property
    def date_of_issue(self):
        return self._date_of_issue

    @date_of_issue.setter
    def date_of_issue(self, val):
        if not Validator.validate_date_pass(val):
            raise AttributeError("Date of issue isn't correct!!!")
        self._date_of_issue = val

    @property
    def date_of_expire(self):
        return self._date_of_expire

    @date_of_expire.setter
    def date_of_expire(self, val):
        if not Validator.validate_date_future(val):
            raise AttributeError("Date of expire isn't correct!!!")
        self._date_of_expire = val

    @property
    def cvc(self):
        return self._cvc

    @cvc.setter
    def cvc(self, val):
        if not Validator.validate_with_regex(CreditCardRegex.cvc_regex, val):
            raise AttributeError("CVC isn't correct!!!")
        self._cvc = val

    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, val):
        if not Validator.validate_with_regex(CreditCardRegex.owner_name_regex, val):
            raise AttributeError("Owner name isn't correct!!!")
        self._owner_name = val

    def input(self):
        K = dict((i, input(i)) for i in dir(self)
                 if not i.startswith("__") and not i.startswith("_") and i != "input")
        for (key, value) in K.items():
            setattr(self, key, K.get(key, value))
        return K
