import requests


response = requests.get('http://icanhazdadjoke.com', params = {'format': 'json'})
print(response.text)
data = response.json()
print(data)
print(data['ip'])

# import json
# data = json.loads(response.text)
# print(data)
# print(data['ip'])
