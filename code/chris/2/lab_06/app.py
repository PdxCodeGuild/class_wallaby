from flask import Flask, render_template, request
from string import ascii_lowercase
app = Flask(__name__)

@app.route('/')
def index():
  rot_input_string = 'test'
  return render_template('index.html', rot_input_string = rot_input_string)

@app.route('/rot13', methods=['POST'])
def rot13():
  result = ''
  lower = ascii_lowercase
  rot_str = request.form['rot13_text']
  for char in rot_str:
    result += lower[(ord(char) - 84) % 26]


  return render_template('rot13.html', result = result)


app.run(debug=True)