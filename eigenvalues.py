from __future__ import division
import numpy as np


def saaty(matrix):
    normal = matrix / matrix.sum(axis=0)
    return normal.mean(1)


def revised(matrix):
    normal = matrix / matrix.max(axis=0)
    return normal.mean(1)


criteria_a = np.matrixlib.matrix([[1, 1/9, 1], [9, 1, 9], [1, 1/9, 1]])
print(saaty(criteria_a))
print(revised(criteria_a))
