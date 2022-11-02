class CardException:
    def __init__(self, exceptions):
        self.exceptions = [exceptions]

    def add_ex(self, ex):
        self.exceptions.append(ex)

    def __str__(self):
        result = ""
        i = 1
        for ex in self.exceptions:
            result += f"{i}: {ex}\n"
        return result

    def to_json(self):
        return {"Exceptions": self.exceptions}
