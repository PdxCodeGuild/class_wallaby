from re import DEBUG
import requests
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def home():
    cities = ['london', 'portland', 'seattle']
    return render_template('index.html', cities = cities)

@app.route('/temperature/', methods= ['POST', 'GET'])
def temperature():
    if request.method == "POST":
        city = request.form.get('selected_city')
        print('CITY', city)
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=884cfd64f3a52a3354c76c381207cf1e')
        coordinates = response.json()
        print(coordinates)
        return render_template('temperature.html', coordinates = coordinates, city= city )
    elif request.method == 'GET':
        return 'A Request was made'


app.run(debug=True)