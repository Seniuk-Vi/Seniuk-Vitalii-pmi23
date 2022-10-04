import re
from datetime import datetime


class Validator:

    @staticmethod
    def validate_with_regex(regex, arg):
        boo = re.fullmatch(regex, str(arg)) is not None
        return boo

    @staticmethod
    def is_in_map(map, value):
        return value in map

    @staticmethod
    def validate_date_pass(input_date):
        date_format = "%d/%m/%Y"
        start = datetime.strptime(input_date, date_format)
        return start <= datetime.now()

    @staticmethod
    def validate_date_future(input_date):
        date_format = "%d/%m/%Y"
        start = datetime.strptime(input_date, date_format)
        return start > datetime.now()

    @staticmethod
    def validateFileName(filename, end=".txt"):
        if not filename.endswith(end):
            raise ValueError("File should end with ." + end)
        return filename
