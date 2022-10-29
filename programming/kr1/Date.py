from Validator import *
from datetime import datetime

date_format: str = "%Y-%m-%d"


class Date:
    def __init__(self, t):
        date = datetime.strptime(t, date_format)
        self.year = date.year
        self.month = date.month
        self.day = date.day

    def __str__(self):
        result = f"{self.year}-{self.month}-{self.day}"

        return result

    def __repr__(self):
        result = ""
        for i in dir(self):
            if not i.startswith("__") and not i.startswith("_") and i != "input":
                result += i + ": " + str(getattr(self, i)) + " "
        return result

    @property
    def year(self):
        return self._year

    @year.setter
    @Validator.decoratorYear
    def year(self, val):
        self._year = val

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, val):
        self._month = val

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, val):
        self._day = val

    def __eq__(self, other):
        return self._year == other.year and self.month == other.month and self.day == other.day

    def __ge__(self, other):
        if self.year > other.year:
            return self.year > other.year
        if self.month > other.month:
            return self.month > other.month
        if self.day > other.day:
            return self.day > other.day
