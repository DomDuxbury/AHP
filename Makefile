curl: 
		curl -H "Content-Type: application/json" -X POST -d \
			'{"journeys": [ { "time": 54, "price": 53, "reliability": 95 }, { "time": 100, "price": 32, "reliability": 96 }, { "time": 60, "price": 70, "reliability": 98 } ], "weights": {"time": 0.1, "price": 0.5, "reliability":0.4}}'\
			http://localhost:5001/rank
