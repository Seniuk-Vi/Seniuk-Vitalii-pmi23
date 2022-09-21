import os
import random

# TASK:
#   Користувач повинен мати 2 опції:
#   1. ввести масив довжини N з клавіатури
#   2. згенерувати довільний масив довжини N зі значень, які знаходяться в діапазоні [a, b], де a,b вводяться з клавіатури.
#   Реалізувати алгоритм mergeSort для сортування даного масиву. Вивести кількість операцій, яка була необхідною для сортування масиву.
#   Програма повинна закінчувати свою роботу тільки у випадку, коли користувач натиснув відповідний пункт меню.


LINE_SEP = os.linesep


class Array:
    """
    Array class
    """

    def __init__(self, *data):
        if len(data) == 1:  # 1
            try:
                self.array = [int(input("number: ")) for i in range(data[0])]
            except ValueError:
                raise ValueError("Wrong array number input!!!")
        elif len(data) == 3:  # 2
            if data[1] > data[2] - 1:
                raise ValueError("Start must be less than end!!!")
            self.array = [random.randint(data[1], data[2] - 1) for i in range(data[0])]
        else:
            raise Exception("Wrong arguments in constructor!!!")
        print(f"Total number of steps: {merge_sort(self.array, 0, len(self.array) - 1)}")


def input_array_size():
    try:
        array_size = int(input("Enter array size[2-30]:"))
        if 2 > array_size or array_size > 30:
            raise ValueError()
    except ValueError:
        raise ValueError("Wrong array size[2-30]!!!")
    return array_size


def console_array():
    """
    Create array from console
    :return: array
    """
    array_size = input_array_size()
    array = Array(array_size)
    return array.array


def random_array():
    """
    Create random array with N length and with numbers in range[start-end]
    :return:
    """
    try:
        a = int(input("Enter start:"))
        b = int(input("Enter end:"))
    except ValueError:
        raise ValueError("Wrong integer input!!!")
    array_size = input_array_size()
    array = Array(array_size, a, b)
    return array.array


def merge(arr, left, m, r):
    merged = []
    count = 0
    i = left
    j = m + 1
    while i <= m and j <= r:
        count += 1
        if arr[i] < arr[j]:
            merged.append(arr[i])
            i += 1
        else:
            merged.append(arr[j])
            j += 1
    while i <= m:
        count += 1
        merged.append(arr[i])
        i += 1
    while j <= r:
        count += 1
        merged.append(arr[j])
        j += 1
    for i in range(left, r + 1):
        count += 1
        arr[i] = merged[i - left]
    return count


def merge_sort(arr, left, r):
    count = 0
    if left >= r:
        return count
    mid = (left + r) >> 1
    count += merge_sort(arr, left, mid)
    count += merge_sort(arr, mid + 1, r)
    count += merge(arr, left, mid, r)
    return count


def choose_next_move():
    try:
        choose = input(
            f"Menu:"
            f"{LINE_SEP} 1- enter array through console."
            f"{LINE_SEP} 2- create array from range."
            f"{LINE_SEP} 3- exit: ")
        options = {"1": console_array, "2": random_array, "3": exit}
        return options[choose]()
    except ValueError as ex:
        raise ex
    except KeyError:
        raise ValueError("Please, enter the correct number!!!")


if __name__ == "__main__":
    new_array = []
    while True:
        try:
            new_array = choose_next_move()
            print(new_array)
        except Exception as exception:
            print(exception)
