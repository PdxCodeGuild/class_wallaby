"""
LISTS
"""
baseball_teams = ['royals', 'cardinals', 'mariners', 'rays', 'orioles']
baseball_teams.append('cubs')

for team in baseball_teams:
	print(team.capitalize())

"""
LIST of DICTIONARIES
"""
baseball_teams = [
	{'name': 'Royals', 'city': 'Kansas City', 'league': 'AL'},
	{'name': 'Cardinals', 'city': 'St. Louis', 'league': 'NL'},
	{'name': 'Mariners', 'city': 'Seattle', 'league': 'AL'},
	{'name': 'Rays', 'city': 'Tampa Bay', 'league': 'AL'},
	{'name': 'Orioles', 'city': 'Baltimore', 'league': 'AL'},
]
baseball_teams.append({'name': 'Cubs', 'city': 'Chicago', 'league': 'NL'})


for team in baseball_teams:
	# The Royals are in Kansas City and play in the AL.
	print(f"The {team['name']} are in {team['city']} and play in the {team['league']}.")