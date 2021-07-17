with open('cities.csv', 'r') as f:
	data = f.read().split('\n')
	for row in data:
		print(row.split(','))

# turn into a list of dictionaries
[
	{'name': 'portland', 'food': 'everything', 'country': 'us', 'climate': 'temperate'},
	{'name': 'kansas city', 'food': 'bbq', 'country': 'us', 'climate': 'temperate'},
	{'name': 'athens', 'food': 'moussaka', 'country': 'greece', 'climate': 'arid'},
]