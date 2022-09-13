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


def appropriation(arr):
    for j in range(1, len(arr)):
        arr[j] += arr[j - 1]
    return arr


def count_amount_of_ways(n):
    """
       Counts number of ways in hexagon
       :argument n: size of hexagon
       :returns Integer
       >>> count_amount_of_ways(2)
       11
       >>> count_amount_of_ways(5)
       259123
    """

    primary_array = [1 for i in range(n)]

    for i in range(n - 1):
        arr = [0 for x in range(len(primary_array) + 1)]
        for j in range(len(primary_array)):
            arr[j] += primary_array[j]
            arr[j + 1] += primary_array[j]
        primary_array = arr
        appropriation(primary_array)

    # add another half
    for i in range(n - 1):
        arr = [0 for x in range(len(primary_array) - 1)]
        for k in range(len(primary_array) - 1):
            arr[k] += primary_array[k]
            arr[k] += primary_array[k + 1]
        primary_array = arr
        appropriation(primary_array)
    return primary_array[-1]


def int_input():
    """
    Operating function that validates input data and handles errors
    """
    while True:
        try:
            n = int(input("Enter size of the hexagonal field(N), exit = 0: "))
            if n == 0:
                break
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
