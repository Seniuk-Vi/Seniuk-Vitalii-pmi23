import os

# TASK:
#   Задано масиви x, y, які складаються з N чисел.
#   Порахувати кількість добутків (xi * yj) <0 і знайти максимальне і мінімальне з них.
#   Всі числа в масивах x, y, які рівні максимальному елементу, замінити на протилежне,
#   а ті числа, які дорівнюють мінімальному, замінити на нулі.


LINE_SEP = os.linesep


class Arrays:
    """
    Array class
    """

    def __init__(self):
        self.array_x = []
        self.array_y = []
        self.max = 0
        self.min = 0
        self.result_arr = []

    def init(self):
        array_x_size = input_array_size("Input first array size:")
        self.array_x = create_array(array_x_size)
        array_y_size = input_array_size("Input second array size:")
        self.array_y = create_array(array_y_size)
        return self

    def product(self):
        self.validate_arrays()
        self.result_arr = []
        for i in [x for x in self.array_x if x < 0]:
            for j in [x for x in self.array_y if x > 0]:
                self.result_arr.append(i * j)
        for i in [x for x in self.array_x if x > 0]:
            for j in [x for x in self.array_y if x < 0]:
                self.result_arr.append(i * j)
        self.max = max(self.result_arr)
        self.min = min(self.result_arr)
        return self

    def replacing(self):
        self.validate_arrays()
        self.replace(self.array_x)
        self.replace(self.array_y)
        return self

    def replace(self, array):
        for i in range(len(array)):
            print(array[i])
            if array[i] == self.max:
                array[i] = -array[i]
            elif array[i] == self.min:
                array[i] = 0

    def validate_arrays(self):
        if len(self.array_x) < 1 or len(self.array_y) < 1:
            raise ValueError("Arrays are empty, init first!!!")


def input_array_size(message):
    try:
        array_size = int(input(message))
        if 0 > array_size or array_size > 31:
            raise ValueError()
    except ValueError:
        raise ValueError("Wrong array size[1-30]!!!")
    return array_size


def create_array(size):
    try:
        new_array = [int(input("number: ")) for i in range(size)]
    except ValueError:
        raise ValueError("Wrong array number input!!!")
    return new_array


def arrays_functions(arrays):
    try:
        choose = input(
            f"Menu:"
            f"{LINE_SEP} 1- create new arrays."
            f"{LINE_SEP} 2- count the number of products (xi * yj) <0 and find the maximum and minimum of them."
            f"{LINE_SEP} 3- Replace all numbers in arrays x, y that are equal to the maximum element with the opposite,"
            f"{LINE_SEP}    and those numbers that are equal to the minimum, replace with zeros: "
            f"{LINE_SEP} 4- exit:")
        options = {"1": arrays.init, "2": arrays.product, "3": arrays.replacing, "4": exit}
        return options[choose]()
    except ValueError as ex:
        raise ex
    except KeyError:
        raise ValueError("Please, enter the correct number!!!")


if __name__ == "__main__":
    arrays = Arrays()
    while True:
        try:
            arrays = arrays_functions(arrays)
            print(f"first array: {arrays.array_x}")
            print(f"second array: {arrays.array_y}")
            print(f"result array: {arrays.result_arr}")
            print(f"Number of elements in (x * y) < 0: {len(arrays.result_arr)}, min: {arrays.min}, max: {arrays.max}")
        except Exception as exception:
            print(exception)
