def get_journeys(n=3):
    return [
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
            'reliability': 98
        },
        {
            'time': 80,
            'price': 65,
            'reliability': 94
        },
        {
            'time': 100,
            'price': 35,
            'reliability': 94
        }
    ][:n]


def get_attrib_dict(w1, w2, w3):
    return {
        'time': {
            'bigger_is_better': False,
            'weight': w1
        },
        'price': {
            'bigger_is_better': False,
            'weight': w2
        },
        'reliability': {
            'bigger_is_better': True,
            'weight': w3,
            'minX': 90,
            'maxX': 100
        }
    }
