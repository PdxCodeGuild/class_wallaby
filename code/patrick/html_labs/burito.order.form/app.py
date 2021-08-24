from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('new-user.html')

@app.route('/tempature/', methods=['POST', 'GET'])
def temperature():
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

app.run(debug=True)


