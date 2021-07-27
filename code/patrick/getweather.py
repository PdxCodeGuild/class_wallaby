import requests
from datetime import datetime
def main():
    city = input('Please enter the city for which you would like the free forecast for: ') 
    user_need = input('Would you like a "point" in time or a "5-day" forcast for the city?: ')
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=884cfd64f3a52a3354c76c381207cf1e') # add &units=imperial
    response_1 = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?q={city}&units=imperial&appid=884cfd64f3a52a3354c76c381207cf1e')

    def one_point(response):
        dict_1 = response.json()
        desc = dict_1['weather'][0]['description']
        temp = dict_1['main']['temp']
        feels =dict_1['main']['feels_like']
        max = dict_1['main']['temp_max']
        min= dict_1['main']['temp_min']
        dt = dict_1['dt']
        dt = int(dt)
        date = datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d %I:%M:%p')

        return print(f'''\nThe weather in {city} for {date} is expected to have {desc}, with a temp of 
        {temp}F which will feel like {feels}F. The max temp during the day will be {max}F and low of {min}F.
        ''')
    def five_day(response):
        i = 0
        r = response.json()
        while True:   
            
            for the in r:
                
                dt = int(r['list'][i]['dt'])
                
                
                date = datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d %I:%M:%p')
                date = date.split(' ')
                temp = r['list'][i]['main']['temp']
                feels =r['list'][i]['main']['feels_like']
                max = r['list'][i]['main']['temp_max']
                min= r['list'][i]['main']['temp_min']
                print(f'For the date of {date[0]} at {date[1]} the expected temp will be {temp}F but will feel like {feels}F. The max temp will be {max}F and the min will be {min}F.')
                i += 1
            if i >= 40:
                break

    if user_need == "point":
        one_point(response)

    elif user_need == "5-day":
        five_day(response_1)
        


    while True:
        again = input('Would you like to enter a new city?: ').lower()
        if again == 'yes' or again == 'y':
            main()
        elif again == 'no' or again == 'n':
            print("Goodbye!")
            exit()
        else:
            print('Enter a valid response!')
            continue

main()

