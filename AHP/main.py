from __future__ import division
import numpy as np
import sys
import config
from normalise import Normaliser
from compare import ExpComparer, SimpleComparer


def calc_matrix(values, norm, comparer):
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
        normal = matrix / matrix.sum(axis=0)
        return normal.mean(axis=1)


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
        values = list(map(lambda x: float(x[attrib]), journeys))
        minX, maxX = getMinMax(attribs, attrib, values)
        norm = Normaliser(minX, maxX)
        comparer = SimpleComparer(attribs[attrib]['bigger_is_better'])

        matrix = calc_matrix(values, norm, comparer)
        weight_vector = calc_weight_vector(matrix)
        global_weights[attrib] = weight_vector * attribs[attrib]['weight']

    global_weights['total'] = (global_weights['price']
                               + global_weights['time']
                               + global_weights['reliability'])

    return global_weights


def report(result, journeys):
    rank = list(enumerate(result['total']))
    rank = sorted(rank, key=lambda x: x[1], reverse=True)
    for journeyId, score in rank:
        journey = journeys[journeyId]
        print('Journey {}:\ntime:\t\t{}\nprice:\t\t{}\nreliability:\t{}\n'
              .format(journeyId + 1, journey['time'],
                      journey['price'], journey['reliability']))
        print('Overall: \t{}'.format(score))
        print('Time:\t\t{}').format(result['time'][journeyId])
        print('Price:\t\t{}').format(result['price'][journeyId])
        print('Reliability:\t{}\n\n').format(result['reliability'][journeyId])


def main():
    time_weight, price_weight, reliability_weight = (float(sys.argv[1]),
                                                     float(sys.argv[2]),
                                                     float(sys.argv[3]))
    attrib_dict = config.get_attrib_dict(time_weight,
                                         price_weight,
                                         reliability_weight)
    journeys = config.get_journeys(3)

    result = calc_all_weights(attrib_dict, journeys)
    report(result, journeys)


if __name__ == '__main__':
    main()
