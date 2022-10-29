import re
from Booking import *
from BookingRegex import *
from datetime import datetime

JSON = "json"


class Validator:

    @staticmethod
    def validate_with_regex(regex, arg):
        boo = re.fullmatch(regex, str(arg)) is not None
        return boo

    @staticmethod
    def decoratorName(func):
        def validateName(self, val):
            if not Validator.validate_with_regex(BookingRegex.name, val):
                raise AttributeError("Name isn't correct!!!")
            return func(self, val)

        return validateName

    @staticmethod
    def decoratorPrice(func):
        def validatePrice(self, val):
            if not Validator.validate_with_regex(BookingRegex.price, val):
                raise AttributeError("Price isn't correct!!!")
            return func(self, val)

        return validatePrice

    @staticmethod
    def decoratorYear(func):
        def validateYear(self, val):
            if not Validator.validate_with_regex(BookingRegex.year, val):
                raise AttributeError("Year isn't correct!!!")
            return func(self, val)

        return validateYear

    @staticmethod
    def decoratorDay(func):
        def validateDay(self, val):
            print(val)
            if not Validator.validate_with_regex(BookingRegex.day, val):
                raise AttributeError("Day isn't correct!!!")
            return func(self, val)

        return validateDay

    @staticmethod
    def decoratorDate(func):
        def validateDate(self, val):
            try:
                date = datetime.strptime("2019-11-20",  "%Y-%m-%d")
                min_date = datetime.strptime("2019-10-23",  "%Y-%m-%d")
                if date < min_date:
                    raise ValueError
            except ValueError:
                raise AttributeError("Date isn't correct!!!")
            return func(self, val)
        return validateDate

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
