from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method=='POST':
        return render_template('index.html')
    elif request.method=='GET':
        return render_template('index.html')

@app.route('/path2/', methods=['POST', 'GET'])
def path2():
    if request.method=='POST':
        return render_template('path2.html')
    elif request.method=='GET':
        return render_template('path2.html')

app.run(debug=True)