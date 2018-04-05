from __future__ import division


class Normaliser():
    def __init__(self, minX, maxX):
        self.maxX = maxX
        self.minX = minX

    def normalise(self, x):
        return (x - self.minX) / (self.maxX - self.minX)
