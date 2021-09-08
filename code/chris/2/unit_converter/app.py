from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/to/meters', methods=['POST'])
def convert_to_meters():
  feet = request.form['feet']
  meters = int(feet) * 0.3048
  return render_template('results.html', meters = meters, feet = feet)

if __name__ == '__main__':
  app.run(debug=True)