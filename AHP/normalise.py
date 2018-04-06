from __future__ import division


class Normaliser():
    def __init__(self, minX, maxX):
        self.maxX = maxX
        self.minX = minX

    def normalise(self, x):
        if self.minX == self.maxX:
            return x
        else:
            return (x - self.minX) / (self.maxX - self.minX)
