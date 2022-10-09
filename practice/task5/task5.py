import os
import time
from FirstStrategy import *
from SecondStrategy import *
from ListStrategy import *
from AmicablePairsIterator import *
from AmicablePairsGenerator import *
from LinkedList import *
import json
from Validator import *

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
error_input_length_message = "Wrong number of pairs [1-15]!!!"


def check_positive(a):
    return a > 0


if __name__ == "__main__":
    am_list = LinkedList()
    strategy = None
    while True:
        try:
            choose = int(input(f"1-First strategy (iterator). "
                               f"{LINE_SEP}2-Second strategy (file)."
                               f"{LINE_SEP}3-Generate elements."
                               f"{LINE_SEP}4-Delete from pos."
                               f"{LINE_SEP}5-Delete in range."
                               f"{LINE_SEP}6-Enter from keyboard."
                               f"{LINE_SEP}7-Add from pos. "
                               f"{LINE_SEP}8-Print list. "
                               f"{LINE_SEP}9-exit"))
            if choose == 1:
                strategy = FirstStrategy()
            if choose == 2:
                strategy = SecondStrategy()
            elif choose == 3:
                am_list = strategy.generate_list(am_list)
            elif choose == 4:
                index_of_elem = int(input("Enter index to be deleted"))
                am_list.delete(index_of_elem)
            elif choose == 5:
                start = int(input("Enter start to be deleted"))
                end = int(input("Enter end to be deleted"))
                for i in range(end-start):
                    am_list.delete(start)
            elif choose == 6:
                data = int(input("Enter element to be added"))
                am_list.append(data)
            elif choose == 7:
                index_of_elem = int(input("Enter index to be added"))
                data = int(input("Enter element to be added"))
                am_list.add(index_of_elem, data)
            elif choose == 8:
                print(am_list.length)
                am_list.print()
            elif choose == 9:
                exit(1)
        except AttributeError as exx:
            print(exx)
        except ValueError as ex:
            print(ex)
