from flask import Flask, redirect, render_template, request

app = Flask(__name__)
units = { 'feet': 0.3048,
          'miles': 1609.34,
          'meters': 1,
          'kilometers': 1000,
          'yards': .9144,
          'inches': .0254}

def converter(distance,distance_choice):
        
  pool = units[distance_choice]

  distance = int(distance)

  total = distance * pool
        
  return total


@app.route('/')
@app.route('/home/', methods= ['POST','GET'])

def home():
  if request.method =='POST':

    distance = request.form['distance']
    print(f'Distance: {distance}')
    distance_choice = request.form['distance_choice'].lower()
    print(f'Distance Choice: {distance_choice}')

    output = converter(distance,distance_choice)
    print(f'output: {output}')
    
    return render_template('index.html', output=output, distance=distance,distance_choice=distance_choice  )

  elif request.method == 'GET': 
    
    return render_template('index.html')
      

 
app.run(debug=True)
