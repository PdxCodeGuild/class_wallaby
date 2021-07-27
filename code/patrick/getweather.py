import requests
from datetime import datetime

city = input('Please enter the city for which you would like the free forecast for: ') 
response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=884cfd64f3a52a3354c76c381207cf1e') # add &units=imperial
dict_1 = response.json()



desc = dict_1['weather'][0]['description']
temp = dict_1['main']['temp']
feels =dict_1['main']['feels_like']
max = dict_1['main']['temp_max']
min= dict_1['main']['temp_min']
dt = dict_1['dt']
dt = int(dt)
date = datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d %I:%M:%p')

print(f'''\nThe weather in {city} for {date} is expected to have {desc}, with a temp of 
{temp}F which will feel like {feels}F. The max temp during the day will be {max}F and low of {min}F.
''')




