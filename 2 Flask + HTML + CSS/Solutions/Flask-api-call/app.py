from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/temperature/', methods=['GET', 'POST'])
def temperature():
    if request.method == 'POST':
        city=request.form['selected_city']
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=884cfd64f3a52a3354c76c381207cf1e')
        coordinates = response.json()
        city = coordinates['name']
        print(coordinates)
        return render_template('temperature.html', coordinates=coordinates, city=city )
    elif request.method == 'GET':
        return 'A GET request was made'

app.run(debug=True)