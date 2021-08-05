import requests


response = requests.get('http://icanhazdadjoke.com', headers = {'accept':'application/json'}) #headers={'Content-Encoding': 'gzip'}
#print(response.apparent_encoding)
x = response.json()
joke_1 = x['joke']#.split('?')
print(joke_1)