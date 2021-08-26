from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    wrap= ['Spinach', 'Wheat Flour', 'White Flour'] 
    rice= ['Brown', 'White', 'None'] 
    bean= ['Black', 'Pinto', 'None']
    protien= ['Carnitas', 'Chicken', 'Sofritas', 'None']
    cheese= ['Cheese', 'Sour Cream']
    return render_template('home-page.html', wrap=wrap, rice=rice, bean=bean, protien=protien, cheese=cheese)

@app.route('/orders/', methods=['POST', 'GET'])
def order_form():
    if request.method == 'POST':
        print('post request')
        wraps = request.form['wrap']
        rice1 = request.form['rice']
        beans= request.form['bean']
        cheese1= request.form['cheese']
        protiens= request.form['protien']
        delivery1= request.form['delivery']
        print(wraps, rice1, beans)
        return render_template('order.html', wraps=wraps, rice1=rice1, beans=beans, cheese1=cheese1, protiens=protiens, delivery1=delivery1)
    
    elif request.method == 'GET':
        return redirect('/')



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


