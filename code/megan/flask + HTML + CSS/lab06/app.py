from flask import Flask, render_template, request
import string

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method=='POST':
        alphabet = string.ascii_lowercase
        number = request.form['number']
        message = request.form['message']
        output = ''
        for letter in message:
            if letter == ' ':
                output += letter
            elif letter != ' ':
                output += alphabet[(alphabet.index(letter)+ 13) % 26]
            print(output)
        return render_template('index.html', number=number, message=message, output=output)
    elif request.method=='GET':
        return render_template('index.html')

app.run(debug=True)

# megancook@Megans-Air lab06 % source env/bin/activate        
# (enc) megancook@Megans-Air lab06 % flask run