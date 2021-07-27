import requests

user_forecast_selection = input("Please enter forecast type (Current or Hourly:  ")
user_city_input = input("Please enter city: ")
if user_forecast_selection == "Current":
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_city_input}&appid=8ede3e88d714311197342701eb01f495")   
    print(response.status_code)
    data =response.json() # install json formatter
    print(data)
if user_forecast_selection == "Hourly":
    response2 = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat=51.5085&lon=-0.1257&exclude=hourly&appid=8ede3e88d714311197342701eb01f495")   
    print(response2.status_code)
    data2 =response2.json() # install json formatter
    print(data2)










