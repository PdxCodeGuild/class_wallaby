import requests

response = requests.get('https://favqs.com/api/qotd')
data = response.json()
#print(data)
quote = data['quote']['body']
author = data['quote']['author']


print(f'Random quote: "{quote}" -{author}')