#!flask/bin/python
import numpy as np
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from main import calc_all_weights, calc_weight_vector
import config


app = Flask(__name__)
CORS(app)


def validate_request(request):
    valid = 'journeys' in request.json \
            and 'comparisons' in request.json
    if not valid:
        abort(400)


def serialize(ranking):
    for key in ranking.keys():
        ranking[key] = list(ranking[key])
    return ranking


def parse_comparisons(comparisons):
    matrix = np.matrix(comparisons)
    return calc_weight_vector(matrix)


@app.route('/rank', methods=['POST'])
def create_task():
    validate_request(request)

    journeys = request.json['journeys']
    comparisons = request.json['comparisons']

    weights = parse_comparisons(comparisons).flatten().tolist()[0]
    attrib_dict = config.get_attrib_dict(*weights)
    ranking = calc_all_weights(attrib_dict, journeys)
    return jsonify({'ranking': serialize(ranking)}), 201


if __name__ == '__main__':
    app.run(debug=True, port=5001)
