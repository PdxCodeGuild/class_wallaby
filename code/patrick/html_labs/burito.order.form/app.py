from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('new-user.html')

@app.route('/tempature/', methods=['POST', 'GET'])
def temperature():
    if request.method == 'POST':
        
        email = request.form['email'] # Jane
       
        print("email username", email)
        return redirect('templates/new-user.html')
    elif request.method == 'GET':
        return 'a GET request was made.'

app.run(debug=True)




