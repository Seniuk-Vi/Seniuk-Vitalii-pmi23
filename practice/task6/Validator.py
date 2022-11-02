import re
from datetime import datetime


class Validator:

    @staticmethod
    def validateFileName(filename, end=".txt"):
        if not filename.endswith(end):
            raise ValueError("File should end with ." + end)
        return filename
