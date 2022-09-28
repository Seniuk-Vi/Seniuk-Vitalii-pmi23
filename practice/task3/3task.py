import os
import time
from LinkedList import *

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


def div_sum(n):
    """
    :param n: number
    :return: all the divisors of a number
    """
    result = LinkedList()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            result.append(i)
            result.append(n // i)
    return result.sum() - n


def amicable_pair(number):
    """
    create list of amicable pairs
    """
    result = LinkedList()
    x = 0
    while True:
        y = div_sum(x)
        if div_sum(y) == x and x != y:
            result.append(x)
            result.append(y)
            if y > x:
                x = y
        if result.length == number:
            break
        x += 1
    return result


def input_size():
    try:
        size = int(input("Enter number of pairs [1-15]:"))
        if 1 > size or size > 15:
            raise ValueError()
    except ValueError:
        raise ValueError("Wrong number of pairs [1-15]!!!")
    return size * 2


if __name__ == "__main__":
    am_list = None
    while True:
        try:
            choose = int(input(f"1-create amicable pairs. {LINE_SEP}2-Enter from keyboard."
                               f"{LINE_SEP}3-Generate random from range[a,b]. {LINE_SEP}4-Add from pos. "
                               f"{LINE_SEP}5-Delete from pos."
                               f" {LINE_SEP}6-Print list. {LINE_SEP}7-exit"))
            if choose == 1:
                start = time.time()
                am_list = amicable_pair(input_size())
                am_list.print()
                print(time.time() - start)
            elif choose == 2:
                number_of_elem = int(input("Enter number of elements"))
                am_list.add_from_keyboard(number_of_elem)
            elif choose == 3:
                number_of_elem = int(input("Enter number of elements"))
                am_list.add_random_from_range(number_of_elem)
            elif choose == 4:
                index_of_elem = int(input("Enter index to be added"))
                data = int(input("Enter element to be added"))
                am_list.add(index_of_elem, data)
            elif choose == 5:
                index_of_elem = int(input("Enter index to be deleted"))
                am_list.delete(index_of_elem)
            elif choose == 6:
                am_list.print()
            elif choose == 7:
                exit()
        except ValueError as ex:
            print(ex)
