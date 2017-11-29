import math


class BaseComparer():
    def __init__(self, bigger_is_better):
        self.bigger_is_better = bigger_is_better

    def compare(self, x, y):
        if self.bigger_is_better:
            return self.equation(x, y)
        else:
            return self.equation(y, x)


class SimpleComparer(BaseComparer):
    def equation(self, x, y):
        return math.floor((y - x) * 8) + 1


class ExpComparer(BaseComparer):
    def equation(self, x, y):
        return math.exp(x) / math.exp(y)
