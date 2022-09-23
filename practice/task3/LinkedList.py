import random

from Node import *


class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def append(self, data):
        self.tail.prev.next = Node(data)
        self.tail.prev.next.prev = self.tail.prev
        self.tail.prev.next.next = self.tail
        self.tail.prev = self.tail.prev.next
        self.length += 1

    def add(self, index, data):
        if index > self.length:
            raise ValueError(f"Index({index}) less than list length({self.length})+1")
        current_node = self.head.next  # can optimize if try to check how it should go from tail or head
        for i in range(index):
            current_node = current_node.next
        current_node.prev.next = Node(data)
        current_node.prev.next.prev = current_node.prev
        current_node.prev = current_node.prev.next
        current_node.prev.next = current_node
        self.length += 1

    def delete(self, index):
        if index + 1 > self.length:
            raise ValueError(f"Index({index}) must be less than list length({self.length})")
        current_node = self.head.next  # can optimize if try to check how it should go from tail or head
        for i in range(index):
            current_node = current_node.next
        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev
        self.length -= 1

    def add_random_from_range(self, number_of_elem):
        a = number_input("Enter start of range")
        b = number_input("Enter end of range")
        if number_of_elem < 1:
            raise ValueError("Number of elements can't be less than 1!!!")
        if a > b:
            raise ValueError("Start must be less than end!!!")
        data = []
        for i in range(number_of_elem):
            data.append(random.randint(a, b))
        self.help_list(number_of_elem, data)

    def add_from_keyboard(self, number_of_elem):
        if number_of_elem < 1:
            raise ValueError("Number of elements can't be less than 1!!!")
        data = []
        for i in range(number_of_elem):
            data.append(number_input("Enter data: "))
        self.help_list(number_of_elem, data)

    def help_list(self, number_of_elem, data):
        head = Node(0)
        current_node = head
        for i in range(number_of_elem):
            current_node.next = Node(data[i])
            print(current_node.next.data)
            current_node.next.prev = current_node
            current_node = current_node.next
        tail = current_node
        self.tail.prev.next = head.next
        head.next.prev = self.tail.prev
        self.tail.prev = tail
        tail.next = self.tail
        self.length += number_of_elem

    def print(self):
        array = []
        current = self.head
        for i in range(self.length):
            array.append(current.next.data)
            current = current.next
        print(array)

    def sum(self):
        summ = 0
        current = self.head
        for i in range(self.length):
            summ += current.next.data
            current = current.next
        return summ


def number_input(message):
    try:
        number = int(input(message))
    except ValueError:
        raise ValueError("Wrong number input!!!")
    return number
