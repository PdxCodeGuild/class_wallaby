from flask import Flask, render_template, request, redirect
# from flask.ext.wtf import Form
# from wtforms import RadioField
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    wrap= ['Spinach', 'Wheat Flour', 'White Flour']  
    rice=['White', 'Brown']
    return render_template('home-page.html', wrap=wrap, rice=rice)

@app.route('/orders/', methods=['POST', 'GET'])
def order_form():
    if request.method == 'POST':
        print('post request')
        wrap = request.form['wrap']
        rice = request.form['rice']
        
        return render_template('order.html', wrap=wrap, rice=rice)
    
    elif request.method == 'GET':
        return redirect('/')
# class SimpleForm(Form):
#     example = RadioField('Label', choices=[('value','description'),('value_two','whatever')])

# # @app.route('/',methods=['post','get'])
# def hello_world():
#     form = SimpleForm()
#     if form.validate_on_submit():
#         print form.example.data
#     else:
#         print form.errors
#     return render_template('example.html',form=form)


@app.route('/login/', methods=['POST', 'GET'])
def login():
    return render_template('login.html')

@app.route('/home/', methods=['POST', 'GET'])
def main():
    return render_template('home-page.html')

@app.route('/register/', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        
        email = request.form['email'] # Jane
        password = request.form['password']
        check_password = request.form['check_password']
        address_1 = request.form['address_1']
        address_2 = request.form['address_2']
        address_city = request.form['address_city']
        address_state = request.form['address_state']
        address_zip = request.form['address_zip']
        # person_age = request.form['person_age'] # 34
        print("email username", email, password, check_password)
        return render_template('user-input.html' ,
        email=email, 
        password=password, 
        check_password=check_password,
        address_1=address_1,
        address_2=address_2,
        address_city=address_city,
        address_state=address_state,
        address_zip=address_zip,
        )
    elif request.method == 'GET':
        return 'a GET request was made.'

# @app.route('/order/', methods=['POST', 'GET'])
# def temperature():
#     if request.method == 'POST':



#     elif request.method == 'GET':
#         return 'a GET request was made.'

app.run(debug=True)


