from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    # return 'Hello world'
    # name = "Bob"
    # temperature = 67
    # nums = [1,2,3]
    # return render_template('index.html', name=name, temperature=temperature, nums=nums)
    if request.method=="POST": 
        contact_name = request.form['input_text']
        print(contact_name)
    return render_template('index.html')

@app.route('/receive_form/', methods=['POST'])
def temperature():
    print(request.form)
    person_name = request.form['person_name']
    person_age = request.form['person_age']
    print(person_age, person_name)
    return redirect('/')


# @app.route('/home/')
# def home():
#     return 'This is the home'

# @app.route('/about/')
# def about():
#     return 'This is the about page'

@app.route('/user/<string:username>')
def home(username):
    return f'hello {username}'

# @app.route('user/<int:post_id>')
# def home(post_id):
#     return f'hello {post_id}'

app.run(debug=True)
