import requests

user_forecast_selection = input("Please enter forecast type (Current or 7 days:  ")
user_city_input = input("Please enter city: ")
if user_forecast_selection == "Current":
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_city_input}&appid=8ede3e88d714311197342701eb01f495")   
    print(response.status_code)
    data =response.json() # install json formatter
    print(data)
if user_forecast_selection == "7 days":
    response2 = requests.get(f"https://api.openweathermap.org/data/2.5/forecast/daily?q={user_city_input}&cnt=7&appid=8ede3e88d714311197342701eb01f495")   
    print(response2.status_code)
    data2 =response2.json() # install json formatter
    print(data2)










