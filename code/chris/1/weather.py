import requests
from keys import openWeather_API_key as key


while True:
  city = input('\nEnter a city name: ')
  state = input('Enter a US state or country 2 letter abbreviation: ')
  main_menu_input = input('''
    Select:
    1)Get current weather
    2)Get 7 day forecast

  ''')
  if main_menu_input == '1':
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city},{state}&APPID={key}')
  elif main_menu_input == '2':
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city},{state}&APPID={key}&cnt=7')

  data = response.json()
  print(data)