from ListStrategy import *
from AmicablePairsIterator import *
from task5 import check_positive
from task5 import error_input_length_message
from LinkedList import LinkedList


class FirstStrategy(ListStrategy):
    def generate_list(self, linked_list: LinkedList):
        n_of_pairs = int(input("Enter number of elements"))
        index = int(input("Enter index to start"))
        iterator = AmicablePairsIter(0)
        if not check_positive(n_of_pairs):
            raise ValueError(error_input_length_message)
        for i in range(n_of_pairs):
            linked_list.add(index, next(iterator))
            index += 1
        return linked_list
