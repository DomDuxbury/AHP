curl: 
		curl -H "Content-Type: application/json" -X POST -d \
			'{"journeys": [ { "time": 54, "price": 53, "reliability": 95 }, { "time": 100, "price": 32, "reliability": 96 }, { "time": 60, "price": 70, "reliability": 98 } ], "comparisons": [ [1,1,1], [1,1,1], [1,1,1] ]}'\
			http://localhost:5001/rank
