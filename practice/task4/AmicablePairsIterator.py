from AmicablePairCheck import *


class AmicablePairsIter:
    def __init__(self, start):
        self.x = start

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            y = div_sum(self.x)
            if check_pair(self.x, y):
                first, second = self.x, y
                if y > self.x:
                    self.x = y
                self.x += 1
                return first, second
            self.x += 1

    def __str__(self):
        return self.x
