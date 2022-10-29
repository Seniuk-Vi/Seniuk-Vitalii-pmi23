import os
from Validator import *
from Date import *

LINE_SEP = os.linesep


class Booking:
    def __init__(self, **array):
        for (key, value) in array.items():
            if Validator.validate_with_regex("^[0-2][0-3]:[0-5][0-9]$", array.get(key, value)):
                setattr(self, key, array.get(key, value))
            else:
                setattr(self, key, array.get(key, value))

    def __str__(self):
        result = ""
        for i in dir(self):
            if not i.startswith("__") and not i.startswith("_") and i != "input":
                result += i + ": " + str(getattr(self, i)) + "\n"
        return result

    def __repr__(self):
        result = f"{self._name}"
        # for i in dir(self):
        #     if not i.startswith("__") and not i.startswith("_") and i != "input":
        #         result += i + ": " + str(getattr(self, i))
        return result

    def __eq__(self, other):
        if self.name == other.name:
            return True
        return False

    def __hash__(self):
        return hash(self.name)

    @property
    def name(self):
        return self._name

    @name.setter
    @Validator.decoratorName
    def name(self, val):
        self._name = val

    @property
    def price_per_day(self):
        return self._price_per_day

    @price_per_day.setter
    @Validator.decoratorPrice
    def price_per_day(self, val):
        self._price_per_day = val

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    @Validator.decoratorDate
    def start_date(self, val):
        try:
            start = Date(val)
        except ValueError as ex:
            raise AttributeError(ex, "Start date isn't correct!!!")
        self._start_date = start

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    @Validator.decoratorDate
    def end_date(self, val):
        try:
            end = Date(val)
            if end.__str__() < self.start_date.__str__():
                raise AttributeError
        except AttributeError as ex:
            raise AttributeError(ex, "End date isn't correct!!!")
        self._end_date = end

    def price(self):
        start = datetime.strptime(self.start_date.__str__(), "%Y-%m-%d")
        end = datetime.strptime(self.end_date.__str__(), "%Y-%m-%d")
        delta = start - end
        count_of_days = delta.days
        if count_of_days == 0:
            return self.price_per_day
        return count_of_days*self.price_per_day

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
