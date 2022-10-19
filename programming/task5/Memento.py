class Memento:

    def __init__(self, mas, file_n):
        self.mas = mas
        self.file_name = file_n

    def getMas(self):
        return self.mas

    def getFileName(self):
        return self.file_name
