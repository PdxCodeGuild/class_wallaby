from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/venues/', methods=['POST', 'GET'])
def venues():
    if request.method=='POST':
        city = request.form.get('selected_city')
        response = requests.get(f'https://api.seatgeek.com/2/venues?city={city}client_id=MjMwNjQ3MjJ8MTYyOTk1MTc3MS4yNTY4OTcy&client_secret=677e6a58213924503cc0d9ecedef678556e4c663670f4f5272e570d630abe066')
        venues = response.json()
        city = venues['name']
        print(venues)
        return render_template('venues.html', venues=venues, city=city)
    elif request.method=='GET':
        return 'venues'

@app.route('/events/', methods=['POST', 'GET'])
def events():
    if request.method=='POST':
        venue_id = request.form.get('selected_venues')
        response = requests.get(f'https://api.seatgeek.com/2/events?venue.id={venue_id}client_id=MjMwNjQ3MjJ8MTYyOTk1MTc3MS4yNTY4OTcy&client_secret=677e6a58213924503cc0d9ecedef678556e4c663670f4f5272e570d630abe066')
        events = response.json()
        venue_id = events['name']
        print(events)
        return render_template('events.html', venue_id=venue_id, events=events)
    elif request.method=='GET':
        return 'events'

app.run(debug=True)