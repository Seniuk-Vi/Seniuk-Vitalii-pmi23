from CreditCard import *
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
        if Validator.is_in_map(self.mas, element) is False:
            self.mas.append(element)

    def search(self, key):
        for_search = Collection()
        key = key.lower()
        for i in self.mas:
            for j in i.__dict__.values():
                if key in j.lower():
                    for_search.add(i)
                    break
        return for_search

    def delete_by_id(self, iden):
        counter = 0
        for i in self.mas:
            if int(i.id) == int(iden):
                counter += 1
                self.mas.remove(i)
        if counter > 0:
            return self.mas
        else:
            print("No element in list with id " + iden)

    def add_element(self):
        element = CreditCard()
        element.input()
        self.mas.append(element)

    def sort(self, field="id"):
        try:
            self.mas = sorted(self.mas, key=lambda product: str(getattr(product, field)).lower())
        except Exception:
            raise ValueError("no such field in class")

    def edit_by_id(self, iden):
        counter = 0
        for i in range(len(self.mas)):
            if int(self.mas[i]._id) == int(iden):
                counter += 1
                new = CreditCard()
                new.input()
                self.mas.insert(i, new)
                self.mas.remove(self.mas[i + 1])
        if counter == 0:
            print("No element in list with ID " + iden)

    def read_json_file(self, file_name):
        Validator.validateFileName(file_name, "json")
        f = open(file_name)
        file = json.load(f)
        for i, card in enumerate(file):
            try:
                self.mas.append(CreditCard(**card))
            except ValueError as e:
                print("Line" + str(i * (len(card) + 1) + 3) + ": " + str(e))
                continue
        f.close()

    def write_in_json_file(self, file_name):
        Validator.validateFileName(file_name, "json")
        with open(file_name, mode='w', encoding='utf-8') as outfile:
            json.dump([ob.__dict__ for ob in self.mas], outfile, ensure_ascii=False)
        outfile.close()
