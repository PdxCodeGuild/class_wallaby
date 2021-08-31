from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method=='POST':
        ...
    return render_template('index.html')

app.run(debug=True)