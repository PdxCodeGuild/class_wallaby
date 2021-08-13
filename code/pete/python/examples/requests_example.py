import requests
import json

"""Get Request to www.python.org"""
# response = requests.get('https://www.python.org/')

# print(response) # <Response [200]>
# print(type(response)) # Response class from requests module
# print(response.status_code) # 200
# print(response.text)

"""CocktailDB API"""

while True:
	search_term = input("What drink do you want? Type 'done' to quit.  ")
	if search_term == 'done':
		break
	params = {
		's': search_term
	}
	response = requests.get('https://www.thecocktaildb.com/api/json/v1/1/search.php', params=params)
	# print(response) # <Response [200]>
	# print(response.text)
	# print(type(response.text)) # <class 'str'>
	data = json.loads(response.text)
	# print(data)
	# print(type(data)) # <class 'dict'>

	drinks = data['drinks']
	if drinks is None:
		print("Sorry, we don't have that one.")
		continue
	# print(drinks)
	# print(type(drinks)) # <class 'list'>

	# print(drinks[0].keys()) # showed us the keys of each dict (so we knew what we could get out of it)

	for drink in drinks:
		print()
		print('🍸', drink['strDrink'])
		print(drink['strInstructions'])
		print()