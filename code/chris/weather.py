import requests


while True:
  city = input('\nEnter a city name: ')
  state = input('Enter a US state or country 2 letter abbreviation: ')
  main_menu_input = input('''
    Select:
    1)Get current weather from city

  ''')
  if main_menu_input == '1':
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=honolulu,hik&APPID=')
    data = response.json()
