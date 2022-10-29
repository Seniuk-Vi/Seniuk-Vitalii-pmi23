from AmicablePairCheck import *


def am_pairs_gen():
    start = 0
    print("start")
    while True:
        y = div_sum(start)
        if check_pair(start, y):
            first, second = start, y
            if y > start:
                start = y
            yield first, second
        start += 1
