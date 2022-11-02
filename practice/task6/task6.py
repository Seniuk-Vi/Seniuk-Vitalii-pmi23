import os
from Observer import Observer
from Logger import Logger
from Event import *
from LinkedList import *
import copy

LINE_SEP = os.linesep
LINE_DIVIDER = "~~~~~~~~~~~~~~~~~~~~~~~~~"
error_input_length_message = "Wrong number of pairs [1-15]!!!"


def check_positive(a):
    return a > 0


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


def add(my_list: LinkedList):
    """add element to pos"""
    old = copy.deepcopy(my_list)
    index = int(input("Enter index"))
    data = int(input("Enter integer"))
    my_list.add(index, data)
    Event("Add", old, my_list, index)


def add_range(my_list: LinkedList):
    """add elements to pos"""
    old = copy.deepcopy(my_list)
    index = int(input("Enter index"))
    n = int(input("Enter number of elements"))
    datas = []
    for i in range(n):
        datas.append(int(input("Enter integer")))
        my_list.add(index + i, datas[i])
    Event("Add", old, my_list, (index, index + n - 1))


def delete(my_list: LinkedList):
    """delete element from pos"""
    old = copy.deepcopy(my_list)
    index = int(input("Enter index"))
    my_list.delete(index)
    Event("Delete", old, my_list, index)


def delete_range(my_list: LinkedList):
    """delete elements from range"""
    old = copy.deepcopy(my_list)
    start = int(input("Enter start"))
    end = int(input("Enter end"))
    for i in range(end - start + 1):
        my_list.delete(start)
    Event("Delete", old, my_list, (start, end))


def print_list(my_list: LinkedList):
    """Pring list"""
    print(my_list)


if __name__ == "__main__":
    my_list = LinkedList()
    observer = Observer()
    observer.add_event("Add", Logger.write_to_file)
    observer.add_event("Delete", Logger.write_to_file)
    while True:
        try:
            program(my_list, add, add_range, delete, delete_range, print_list, exit)
        except Exception as ex:
            print(ex)
