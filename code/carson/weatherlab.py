""" have user pick from list of infomation to display

i.e daily, weekly, and monthly forcast

"""





import requests
print(' Search for a city to get the weather ! :)')
state = input('State: ')
city = input(" City:  ")
print(city)
response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city},{state}&units=imperial&appid=b55c99ab16c500de4bf79dd8c45ef232')

data = response.json()
print(data)
temp = data['main']['temp']
des = data['weather'][0]['description']
#print(des)
loc = data['name']
#print(loc)
print(f' The weather in {loc} is {temp} degrees with {des} ')
                                   