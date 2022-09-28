import os
import numpy as np

LINE_SEP = os.linesep


class Matrix:
    def __init__(self):
        self.matrix = None
        self.array = None

    def create_array(self):
        """Create start array"""
        arr_size = number_input("Enter array size")
        if arr_size < 0:
            raise ValueError("Wrong array size!!!")
        try:
            self.array = [int(input("number: ")) for i in range(arr_size)]
        except ValueError:
            raise ValueError("Wrong array number input!!!")

    def create_matrix(self):
        """Create matrix"""
        if self.array is None:
            raise ValueError("First create array!!!")
        copy_array = self.array.copy()
        med_array = copy_array.copy()
        for i in range(len(self.array) - 1):
            move_elem = copy_array[0]
            copy_array.pop(0)
            copy_array.append(move_elem)
            med_array += copy_array
        self.matrix = np.array(med_array).reshape(len(self.array), len(self.array))

    def print_matrix(self):
        """Print matrix"""
        if self.matrix is None:
            raise ValueError("Create matrix first!!!")
        print(self.matrix)


def number_input(message):
    try:
        number = int(input(message))
    except ValueError:
        raise ValueError("Wrong number input!!!")
    return number


def program(*functions):
    """works only with class functions"""
    try:
        options = {}
        i = 0
        message = "Menu:"
        for i in range(len(functions)):
            options[i] = functions[i]
            message += f"{LINE_SEP} {i}- {functions[i].__doc__}."
        options[i + 1] = exit
        choose = int(input(message))
        return options[choose]()
    except KeyError:
        raise ValueError("Please, enter the correct number!!!")


def close_app():
    """Close program"""
    exit()


if __name__ == "__main__":
    matrix = Matrix()
    while True:
        try:
            program(matrix.create_array, matrix.create_matrix, matrix.print_matrix, close_app)
        except ValueError as ex:
            print(ex)
