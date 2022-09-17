import os
import time

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


def sum_factors(n):
    """
    :param n: number
    :return: all the divisors of a number
    """
    result = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            result.extend([i, n // i])
    return sum(set(result) - {n})


def amicable_pair(number):
    """
    :param number: number of amicable pairs to be counted
    :return: list of tuples
    """
    result = []
    x = 0
    while True:
        y = sum_factors(x)
        if sum_factors(y) == x and x != y:
            result.append(tuple(sorted((x, y))))
        if len(result) == number:
            break
        x += 1
    return set(result)


def input_size():
    try:
        size = int(input("Enter number of pairs [1-15]:"))
        if 0 > size or size > 16:
            raise ValueError()
    except ValueError:
        raise ValueError("Wrong number of pairs [2-15]!!!")
    return size*2


if __name__ == "__main__":
    while True:
        try:

            start = time.time()
            print(amicable_pair(input_size()))
            print(time.time() - start)
        except ValueError as ex:
            print(ex)
