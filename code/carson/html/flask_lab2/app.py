from flask import Flask, render_template, request, redirect
app = Flask(__name__)
units = { 'feet': 0.3048,
          'miles': 1609.34,
          'meters': 1,
          'kilometers': 1000,
          'yards': .9144,
          'inches': .0254}




@app.route('/')
@app.route('/home/', methods=['POST'])
def home():

        # distance_choice = input

        # pool = units[distance_choice]

        # distance = input

        # distance = int(distance)

        # total = distance * pool

  return render_template('index.html')




    
app.run(debug=True)