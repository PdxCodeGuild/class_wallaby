# https://openweathermap.org/current

import requests

# api_key = '1128f4f2ee85b1109fc9c6b1880d0a86'

# city = input('Enter city: ')
# state = input('Enter state (ex: WA): ')

'''
parameters = {
    'city': 'Vancouver', 
    'state': 'WA'
}
'''

# current weather
response = requests.get('api.openweathermap.org/data/2.5/weather?q=Vancouver,WA&appid=1128f4f2ee85b1109fc9c6b1880d0a86')
# response = requests.get('api.openweathermap.org/data/2.5/weather?q=Vancouver,WA&appid=1128f4f2ee85b1109fc9c6b1880d0a86' params = parameters)
print(response.status_code)

data = response.json()
print(data)

# print('MY ID', data['id'])

# daily forecast 7 days

# national weather alerts 