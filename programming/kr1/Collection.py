from Booking import *
from Validator import *
import json


class Collection:
    def __init__(self):
        self.mas = []

    def __setitem__(self, floor_number, data):
        self.mas[floor_number] = data

    def __getitem__(self, key):
        return self.mas[key]

    def __len__(self):
        return len(self.mas)

    def __str__(self):
        x = ""
        for i in self.mas:
            x += str(i) + "\n"
        return x

    def add(self, element):
        if not Validator.is_in_map(self.mas, element):
            self.mas.append(element)

    @Validator.decoratorJsonFile
    def read_json_file(self, file_name):
        f = open(file_name)
        file = json.load(f)
        for i, card in enumerate(file):
            try:
                self.mas.append(Booking(**card))
            except AttributeError as ex:
                print("Line" + str(i * (len(card) + 1) + 3) + ": " + str(ex))
        f.close()
        self.file_name = file_name

    @Validator.decoratorJsonFile
    def write_in_json_file(self, file_name):
        with open(file_name, mode='w', encoding='utf-8') as outfile:
            json.dump([ob.__dict__ for ob in self.mas], outfile, ensure_ascii=False)
        outfile.close()

    def count_price(self, name):
        for i in self.mas:
            if i.name == name:
                return i.price()
