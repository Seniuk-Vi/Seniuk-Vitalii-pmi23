from CreditCard import *
from Validator import *
from Originator import *
from CareTaker import *
import json
import copy


class Collection:
    def __init__(self):
        self.file_name = "input.json"
        self.mas = []
        self.originator = Originator()
        self.care_taker = CareTaker(self.originator, 5, self)

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

    def copy(self, memento: Memento):
        self.mas = memento.getMas()
        self.file_name = memento.getFileName()
        self.update_json()

    def save(self):
        self.originator._state = copy.deepcopy(self)
        self.care_taker.create()
        self.update_json()

    def undo(self):
        self.care_taker.undo()

    def redo(self):
        self.care_taker.redo()

    def add(self, element):
        if not Validator.is_in_map(self.mas, element):
            self.mas.append(element)
        self.update_json()

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
        self.update_json()

    def add_element(self):
        element = CreditCard()
        element.input()
        self.mas.append(element)

    def sort(self, field="id"):
        try:
            self.mas = sorted(self.mas, key=lambda product: str(getattr(product, field)).lower())
        except Exception:
            raise ValueError("no such field in class")
        self.update_json()

    def edit_by_id(self, iden):
        counter = 0
        try:
            for i in range(len(self.mas)):
                if int(self.mas[i].id) == int(iden):
                    counter += 1
                    new = CreditCard()
                    new.input()
                    self.mas.insert(i, new)
                    self.mas.remove(self.mas[i + 1])
            if counter == 0:
                print("No element in list with ID " + iden)
            self.update_json()
        except Exception as ex:
            print(ex)

    def update_json(self):
        with open(self.file_name, mode='w', encoding='utf-8') as outfile:
            json.dump([ob.__dict__ for ob in self.mas], outfile, ensure_ascii=False)
        outfile.close()

    @Validator.decoratorJsonFile
    def read_json_file(self, file_name):
        f = open(file_name)
        file = json.load(f)
        for i, card in enumerate(file):
            try:
                cardd = CreditCard(**card)
                if not Validator.is_in_map(self.mas, cardd):
                    self.mas.append(cardd)
                else:
                    raise AttributeError("Id is already in use")
            except AttributeError as ex:
                print("Line" + str(i * (len(card) + 1) + 3) + ": " + str(ex))
        f.close()
        self.file_name = file_name

    @Validator.decoratorJsonFile
    def write_in_json_file(self, file_name):
        self.file_name = file_name
        self.update_json()
