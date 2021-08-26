from flask import (
    Blueprint, flash, Flask, g, redirect, render_template, request, session, url_for, request, redirect
)
import requests
from datetime import datetime
app = Flask(__name__, instance_relative_config=True)

@app.route('/', methods=['POST', 'GET'])
def home():   
    return render_template('city-search.html', )


@app.route('/search/', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
       
        city = request.form['search']
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=884cfd64f3a52a3354c76c381207cf1e')
        # dict_1 = response.json()
        # print(city, dict_1)
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

            return f'''\nThe weather in {city} for {date} is expected to have {desc}, with a temp of 
            {temp}F which will feel like {feels}F. The max temp during the day will be {max}F and low of {min}F.
            '''
        results = one_point(response)
        print(results)
        return render_template('weather_results.html', results=results)

    elif request.method == 'GET':
        return redirect('/')



    
   





app.run(debug=True)