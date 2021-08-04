from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/temperature/', methods=['GET', 'POST'])
def temperature():
    if request.method == 'POST':
        city=request.form['selected_city']
        return render_template('temperature.html', city=city )
    elif request.method == 'GET':
        return 'A GET request was made'

app.run(debug=True)