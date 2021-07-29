# https://openweathermap.org/current
# api_key = '1128f4f2ee85b1109fc9c6b1880d0a86'

import requests


print("""
    Selections
    
    1 - current weather
    2 - 7 day forecast
    3 - national weather alerts 

    """)

while True:
    command = input("Enter a selection or 'exit' to quit: ")
    if command == exit:
        break
    # current weather
    elif command == 1:
        city = input('Enter city: ')
        state = input('Enter state (ex: WA): ')
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city},{state}&appid=1128f4f2ee85b1109fc9c6b1880d0a86')
        print(response.status_code)
        data = response.json()
        print(data)
    # 7 day forecast
    elif command == 2:
        lat = input('Enter latitude: ')
        lon = input('Enter longitude: ')
        response = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,alerts&appid=1128f4f2ee85b1109fc9c6b1880d0a86')
        print(response.status_code)
        data = response.json()
        print(data)
    # national weather alerts 
    elif command == 3:
        lat = input('Enter latitude: ')
        lon = input('Enter longitude: ')
        response = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily&appid=1128f4f2ee85b1109fc9c6b1880d0a86')
        print(response.status_code)
        data = response.json()
        print(data)
    else:
        print('Please enter a valid selection: 1, 2, or 3')