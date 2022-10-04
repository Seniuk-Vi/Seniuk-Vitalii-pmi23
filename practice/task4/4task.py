import os
import time
from LinkedList import *
from AmicablePairsIterator import *
from AmicablePairsGenerator import *

# TASK:
#  Згенерувати послідовність дружніх чисел розмірності n.
#  Дружніми числами називають два натуральні числа такі,
#  що сума всіх дільників першого (за винятком самого числа) дорівнює другому числу,
#  а сума всіх дільників другого числа (за винятком самого числа) дорівнює першому числу.
#  Наприклад для 220 такими дільниками є числа 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
#  і 110 сума яких рівна 284,
#  а для 284 дільниками є 1, 2, 4, 71, і 142 сума яких рівна 220.
#  Отже (220,284) є парою дружніх чисел.


LINE_SEP = os.linesep
input_length_message = "Enter number of pairs [1-15]:"
error_input_length_message = "Wrong number of pairs [1-15]!!!"


def am_pairs_generator(size):
    result = LinkedList()
    generator = am_pairs_gen()
    while result.length < size:
        result.append(next(generator))
    return result


def am_pairs_iterator(size):
    result = LinkedList()
    iterator = AmicablePairsIter(0)
    while result.length < size:
        result.append(next(iterator))
    return result


def input_number(message="", error_message=""):
    try:
        size = int(input(message))
        if 1 > size or size > 15:
            raise ValueError(error_message)
    except ValueError:
        raise ValueError()
    return size


if __name__ == "__main__":
    am_list = None
    while True:
        try:
            choose = int(input(f"1-create amicable pairs (iterator). "
                               f"{LINE_SEP}2-Create amicable pairs (generator)."
                               f"{LINE_SEP}3-Enter from keyboard."
                               f"{LINE_SEP}4-Generate random from range[a,b]. "
                               f"{LINE_SEP}5-Add from pos. "
                               f"{LINE_SEP}6-Delete from pos."
                               f"{LINE_SEP}7-Print list. "
                               f"{LINE_SEP}8-exit"))
            if choose == 1:
                start = time.time()
                am_list = am_pairs_iterator(input_number(input_length_message, error_input_length_message))
                print(time.time() - start)
            if choose == 2:
                start = time.time()
                am_list = am_pairs_generator(input_number(input_length_message, error_input_length_message))
                print(time.time() - start)
            elif choose == 3:
                number_of_elem = int(input("Enter number of elements"))
                am_list.add_from_keyboard(number_of_elem)
            elif choose == 4:
                number_of_elem = int(input("Enter number of elements"))
                am_list.add_random_from_range(number_of_elem)
            elif choose == 5:
                index_of_elem = int(input("Enter index to be added"))
                data = int(input("Enter element to be added"))
                am_list.add(index_of_elem, data)
            elif choose == 6:
                index_of_elem = int(input("Enter index to be deleted"))
                am_list.delete(index_of_elem)
            elif choose == 7:
                am_list.print()
            elif choose == 8:
                exit()
        except ValueError as ex:
            print(ex)
