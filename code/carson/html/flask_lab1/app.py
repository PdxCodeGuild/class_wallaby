from flask import Flask, render_template, request, redirect
app = Flask(__name__)
import string




@app.route('/')
@app.route('/home/', methods=['POST'])
def home():
  return render_template('index.html ')

@app.route('/cypher/', methods=['POST','GET'])
def cypher():
  if request.method == 'POST':
    user = request.form['user']  
    print(f'user:{user}')
    all = ''
    dict = {}
    abc = string.ascii_lowercase
    
    for i, char in enumerate(abc):
      dict[char] = abc[(i + 13) % 26]

    for i, char in enumerate(user):
      
      all += dict[char]
    print(f'print: {all}')
    return render_template('index.html', all = all)
 
  elif request.method == 'GET':
    return render_template('index.html')

    
    
app.run(debug=True)