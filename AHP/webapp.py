#!flask/bin/python
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from main import calc_all_weights
import config


app = Flask(__name__)
CORS(app)


def validate_request(request):
    valid = 'journeys' in request.json \
            and 'weights' in request.json
    if not valid:
        abort(400)


def serialize(ranking):
    for key in ranking.keys():
        ranking[key] = list(ranking[key])
    return ranking


@app.route('/rank', methods=['POST'])
def create_task():
    validate_request(request)

    journeys = request.json['journeys']
    weights = request.json['weights']

    attrib_dict = config.get_attrib_dict(weights['time'],
                                         weights['price'],
                                         weights['reliability'])
    ranking = calc_all_weights(attrib_dict, journeys)
    return jsonify({'ranking': serialize(ranking)}), 201


if __name__ == '__main__':
    app.run(debug=True, port=5001)
