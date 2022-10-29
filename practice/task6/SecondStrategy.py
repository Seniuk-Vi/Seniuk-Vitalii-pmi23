from ListStrategy import *
from Validator import *
from LinkedList import LinkedList
import json


class SecondStrategy(ListStrategy):
    def generate_list(self, linked_list: LinkedList):
        file_name = input("Enter file name")
        index = int(input("Enter index to start"))
        Validator.validateFileName(file_name, "json")
        f = open(file_name)
        file = json.load(f)
        try:
            for j in file["list"]:
                linked_list.add(index, int(j))
                index += 1
        except ValueError as exception:
            raise ValueError(exception)
        f.close()
        return linked_list
