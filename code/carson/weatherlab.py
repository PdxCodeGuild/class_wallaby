""" have user pick from list of infomation to display

i.e current, weekly, and monthly forcast

"""

import requests

print(' Search for a city to get the weather ! :)')
state = input('State: ')
city = input(' City:  ')
choices = [1,2,3]

response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city},{state}&units=imperial&appid=b55c99ab16c500de4bf79dd8c45ef232')
data = response.json()

lon = data['coord']['lon']
lat = data['coord']['lat']


response2 = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=imperial&appid=b55c99ab16c500de4bf79dd8c45ef232')
data2 = response2.json()

print(data2)


while True:
    choice =input(f'what data would you like to see? \n1 - Current Weather \n2 - Hourly Forcast \n3 - Forcast for 7 days \nInput: ')
    choice = int(choice)
    
    if choice == 1:
        temp = data['main']['temp']
        des = data['weather'][0]['description']
        loc = data['name']
        print(f' The weather in {loc} is {temp} degrees with {des} ')
        break

    #if choice == 2:




#print(des)
        
#print(loc)
        
                    