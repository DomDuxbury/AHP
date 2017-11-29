from __future__ import division
import numpy as np
import sys
from normalise import Normaliser
from compare import ExpComparer, SimpleComparer


def calc_matrix(values, norm, bigger_is_better=True):

    comparer = ExpComparer(bigger_is_better)

    matrix_shape = (len(values), len(values))
    matrix = np.ones(matrix_shape)

    for i, row in enumerate(matrix):
        values[i] = norm.normalise(values[i])

    for i in range(0, len(matrix)):
        for j in range(i+1, len(matrix)):
            matrix[i][j] = comparer.compare(values[i], values[j])
            matrix[j][i] = 1 / matrix[i][j]

    return matrix


def calc_weight_vector(matrix):
        normal_weights = matrix / matrix.sum(axis=0)
        weight_vector = normal_weights.mean(axis=1)
        return weight_vector


def getMinMax(attribs, attrib, values):
    if 'maxX' not in attribs[attrib].keys():
        maxX = max(values)
    else:
        maxX = attribs[attrib]['maxX']

    if 'minX' not in attribs[attrib].keys():
        minX = min(values)
    else:
        minX = attribs[attrib]['minX']

    return minX, maxX


def calc_all_weights(attribs, journeys):
    global_weights = {}

    for attrib in attribs.keys():
        values = map(lambda x: x[attrib], journeys)
        bigger_is_better = attribs[attrib]['bigger_is_better']

        minX, maxX = getMinMax(attribs, attrib, values)
        norm = Normaliser(minX, maxX)

        matrix = calc_matrix(values, norm, bigger_is_better=bigger_is_better)
        weight_vector = calc_weight_vector(matrix)
        global_weights[attrib] = weight_vector * attribs[attrib]['weight']

    return global_weights


def main():
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
            'weight': float(sys.argv[3]),
            'minX': 90,
            'maxX': 100
        }
    }

    global_weights = calc_all_weights(attrib_dict, journeys)

    total = (global_weights['price']
             + global_weights['time']
             + global_weights['reliability'])

    print(global_weights)
    print(total)


if __name__ == '__main__':
    main()
