import os

from Validator import *
from CreditCardRegex import *
from Banks import *

LINE_SEP = os.linesep


class CreditCard:
    def __init__(self, **array):
        errors = []
        for (key, value) in array.items():
            try:
                setattr(self, key, array.get(key, value))
            except AttributeError:
                errors.append(f"Wrong param: {key} ==> {value}")
        if errors:
            raise AttributeError(errors)

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
    @Validator.decoratorId
    def id(self, val):
        if not Validator.validate_with_regex(CreditCardRegex.id_regex, val):
            raise AttributeError("ID isn't correct!!!")
        self._id = val

    @property
    def bank(self):
        return self._bank

    @bank.setter
    @Validator.decoratorBank
    def bank(self, val):
        self._bank = val

    @property
    def card_number(self):
        return self._card_number

    @card_number.setter
    @Validator.decoratorCard
    def card_number(self, val):
        self._card_number = val

    @property
    def date_of_issue(self):
        return self._date_of_issue

    @date_of_issue.setter
    @Validator.decoratorDatePass
    def date_of_issue(self, val):
        self._date_of_issue = val

    @property
    def date_of_expire(self):
        return self._date_of_expire

    @date_of_expire.setter
    @Validator.decoratorDateFuture
    def date_of_expire(self, val):
        self._date_of_expire = val

    @property
    def cvc(self):
        return self._cvc

    @cvc.setter
    @Validator.decoratorCvc
    def cvc(self, val):
        if not Validator.validate_with_regex(CreditCardRegex.cvc_regex, val):
            raise AttributeError("CVC isn't correct!!!")
        self._cvc = val

    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    @Validator.decoratorName
    def owner_name(self, val):
        self._owner_name = val

    def input(self):
        errors = []
        res = dict((i, input(i)) for i in dir(self)
                   if not i.startswith("__") and not i.startswith("_") and i != "input")
        for (key, value) in res.items():
            try:
                setattr(self, key, res.get(key, value))
            except AttributeError:
                errors.append(f"Wrong param: {key} ==> {value}")
        if errors:
            raise AttributeError(errors)
        return res
