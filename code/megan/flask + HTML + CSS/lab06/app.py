from flask import Flask, render_template, request
import string

app = Flask(__name__)

@app.route('/', methods=['POST'])
def home():
    alphabet = string.ascii_lowercase
    number = request.form['number']
    message = request.form['message']
    output = ''
    for letter in message:
        if letter == ' ':
            output += letter
        elif letter != ' ':
            output += alphabet[(alphabet.index(letter)+ 13) % 26]
    return render_template('index.html', number=number, message=message)

app.run(debug=True)