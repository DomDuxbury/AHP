from __future__ import division
import numpy as np
import sys
import math
from normalise import Normaliser
from compare import ExpComparer, SimpleComparer

journeys = [
    {
        'time': 54,
        'price': 53,
        'reliability': 95
    },
    {
        'time': 100,
        'price': 32,
        'reliability': 96
    },
    {
        'time': 60,
        'price': 70,
        'reliability': 99
    }
]


def normalise(x, y, maxX, minX, sign=1):
    value = (x - y) / (maxX - minX)
    value = 8 * sign * value
    if value > 0:
        return math.floor(value + 1)
    else:
        return 1 / math.floor((1 - value))


def normalise_revised(x, maxX, minX):
    return (x - minX) / (maxX - minX)


def calc_matrix(values, bigger_is_better=True):

    norm = Normaliser(max(values), min(values))
    comparer = SimpleComparer(bigger_is_better)

    matrix_shape = (len(values), len(values))
    matrix = np.ones(matrix_shape)

    for i, row in enumerate(matrix):
        print(values[i])
        values[i] = norm.normalise(values[i])
        print(values[i])

    for i in range(0, len(matrix)):
        for j in range(i+1, len(matrix)):
            matrix[i][j] = comparer.compare(values[i], values[j])
            matrix[j][i] = 1 / matrix[i][j]

    return matrix


def calc_all_weights(attribs, journeys):
    global_weights = {}

    for attrib in attribs.keys():
        values = map(lambda x: x[attrib], journeys)
        bigger_is_better = attribs[attrib]['bigger_is_better']
        matrix = calc_matrix(values, bigger_is_better=bigger_is_better)
        weight_vector = calc_weight_vector(matrix)

        global_weights[attrib] = weight_vector * attribs[attrib]['weight']

    return global_weights


def calc_weight_vector(matrix):
        normal_weights = matrix / matrix.sum(axis=0)
        weight_vector = normal_weights.mean(axis=1)
        return weight_vector


def main():
    attrib_dict = {
        'time': {
            'bigger_is_better': False,
            'weight': float(sys.argv[1])
        },
        'price': {
            'bigger_is_better': False,
            'weight': float(sys.argv[2])
        },
        'reliability': {
            'bigger_is_better': True,
            'weight': float(sys.argv[3])
        }
    }
    global_weights = calc_all_weights(attrib_dict, journeys)
    total = (global_weights['price']
             + global_weights['time']
             + global_weights['reliability'])
    print(total)


if __name__ == '__main__':
    main()
