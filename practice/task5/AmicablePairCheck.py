from LinkedList import *


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


def check_pair(x, y):
    """
    Check if x and y is amicable
    """
    while True:
        y = div_sum(x)
        if div_sum(y) == x and x != y:
            return True
        return False
