from Booking import *
from Collection import *
import json

LINE_SEP = os.linesep
LINE_DIVIDER = "~~~~~~~~~~~~~~~~~~~~~~~~~"


def program(col, *functions):
    """works only with class functions"""
    try:
        options = {}
        i = 0
        message = f"{LINE_DIVIDER}{LINE_SEP}Menu:"
        for i in range(len(functions)):
            options[i] = functions[i]
            message += f"{LINE_SEP} {i}- {functions[i].__doc__}."
        options[i + 1] = exit
        message += LINE_SEP + LINE_DIVIDER + LINE_SEP
        choose = int(input(message))
        return options[choose](col)
    except ValueError as ex:
        raise ValueError("Please, enter the correct number!!!", ex)
    except KeyError:
        raise ValueError("Please, enter the correct number!!!")


def input_from_json(coll):
    """read from json"""
    Collection.read_json_file(coll, input("file name:"))


def write_to_json(coll):
    """write to json"""
    Collection.write_in_json_file(coll, input("Enter file name: "))


def print_collection(coll:Collection):
    """print collection"""
    print(coll)


def cont_all_price(coll: Collection):
    """count price by name in collection"""
    print(coll.count_price(input("Enter name: ")))


if __name__ == '__main__':
    collection = Collection()
    try:
        collection.read_json_file("input.json")
    except AttributeError as ex:
        print(ex)
    while True:
        try:
            program(collection, input_from_json, write_to_json, print_collection, cont_all_price)
        except AttributeError as ex:
            print(ex)
