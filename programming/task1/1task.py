import doctest


# TASK:
#   Уявіть собі бджолині стільники - поле з шестикутних клітин зі стороною N. У верхній лівій клітці A
#   знаходиться бджілка. За один хід вона може переповзти на клітку вниз, на клітину вниз-вправо або на клітку
#   вгору-вправо (вгору і вліво бджілка не плазує). Потрібно написати програму, яка знайде кількість способів,
#   якими бджілка може доповзти з клітки A в протилежну клітку B.
#
#   Вхідні дані:
#       Ввести з клавіатури єдине число N - розмір шестикутного поля (2 ≤ N ≤ 12).

#   Вихідні дані:
#       Вивести на екран єдине ціле число - кількість способів.


def count_amount_of_ways(n):
    """
    Counts number of ways in hexagon
    Formula is ==> (k*3)-(5*(n-1)+3), k - number of cells in hexagon
    :argument n: size of hexagon
    :returns Integer
    >>> count_amount_of_ways(2)
    12
    >>> count_amount_of_ways(3)
    42
    """
    k = 1 + 6 * (n * (n - 1) / 2)
    result = (k * 3) - (6 * (n - 1) + 3)
    return int(result)


def int_input():
    """
    Operating function that validates input data and handles errors
    """
    while True:
        try:
            n = int(input("Enter size of the hexagonal field(N): "))
            if n < 2 or n > 12:
                print("Input must be between 2 and 12")
                continue
        except ValueError:
            print("Please, enter the correct number [2,12]!")
            continue
        print("There are %d different ways to get from A to B." % (count_amount_of_ways(n)))


if __name__ == "__main__":
    doctest.testmod()
    int_input()
