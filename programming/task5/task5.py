from Collection import *
from CreditCard import *

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
        message+=LINE_SEP+LINE_DIVIDER+LINE_SEP
        choose = int(input(message))
        return options[choose](col)
    except ValueError as ex:
        raise ValueError("Please, enter the correct number!!!", ex)
    except KeyError:
        raise ValueError("Please, enter the correct number!!!")


def search(coll):
    """search in collection"""
    print(Collection.search(coll, input("Search: ")))


def sort(coll):
    """sort collection"""
    Collection.sort(coll, input("Enter field to sort: "))


def delete_el(coll):
    """delete element from collection"""
    Collection.delete_by_id(coll, input("Enter id: "))


def edit_el(col):
    """edit element from collection"""
    Collection.edit_by_id(col, input("Enter id:"))


def print_col(coll):
    """print collection"""
    print(coll)


def input_from_json(coll):
    """read from json"""
    Collection.read_json_file(coll, input("file name:"))


def write_to_json(coll):
    """write to json"""
    Collection.write_in_json_file(coll, input("Enter file name: "))


def add_to_coll(coll):
    """Add card to collection"""
    card = CreditCard()
    card.input()
    coll.add(card)


def exit_program(coll):
    """exit"""
    exit(0)


def save_col(coll: Collection):
    """Save collection"""
    coll.save()


def undo(coll: Collection):
    """Undo collection"""
    coll.undo()


def redo(coll: Collection):
    """Redo collection"""
    coll.redo()


if __name__ == "__main__":
    collection = Collection()
    collection.read_json_file("input.json")
    collection.save()

    while True:
        try:
            program(collection, save_col, undo, redo, add_to_coll, input_from_json, write_to_json, search, sort,
                    print_col, edit_el,
                    delete_el, exit_program)
        except Exception as ex:
            print (ex)
