# https://openweathermap.org/price
# api_key = 'xyz'

import requests


print("""
    Selections
    
    1 - current weather
    2 - 7 day forecast
    3 - national weather alerts 

    """)

while True:
    command = input("Enter a selection or type 'exit' to quit: ")
    # current weather
    if command == '1':
        # city = input('Enter city name: ')
        # state = input('Enter state (ex: WA): ')
        lat = input('Enter latitude: ')
        lon = input('Enter longitude: ')
        # response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city},{state}&appid=xyz')
        response = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&appid=xyz')
        # print(response.status_code)
        data = response.json()
        # print(type(response))
        # print(response)
        #print(data['current'])
        # print(response.json())
        print(data)
    # 7 day forecast
    elif command == '2':
        lat = input('Enter latitude: ')
        lon = input('Enter longitude: ')
        response = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,alerts&appid=xyz')
        # print(response.status_code)
        data = response.json()
        print(data)
    # national weather alerts 
    elif command == '3':
        lat = input('Enter latitude: ')
        lon = input('Enter longitude: ')
        response = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily&appid=xyz')
        # print(response.status_code)
        data = response.json()
        print(data)
    elif command == 'exit':
        break
    else:
        print('Please enter a valid selection: 1, 2, or 3')