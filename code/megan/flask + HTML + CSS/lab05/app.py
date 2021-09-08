from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    # return 'hello'
    if request.method=='POST':
        # name = request.form.get('name')
        # burrito = request.form.get('burrito')
        # print(burrito)
        return render_template('index.html')
    elif request.method=='GET':
        return render_template('index.html')

@app.route('/review/', methods=['POST', 'GET'])
def review():
    # return 'working'
    # order = []
    if request.method=='POST':
        name = request.form.get('name')
        meat = request.form.get('meat')
        rice = request.form.get('rice')
        beans = request.form.get('beans')
        cheese = request.form.get('cheese')
        extras = request.form.getlist('extras')
        # order = (meat + ', ' + rice + ', ' + beans + ', ' + cheese + ', ' + extras)
        order = [meat, rice, beans, cheese, extras]
        print(order)
        # order_summary = order.append
        return render_template('review.html', name=name, order=order)
    elif request.method=='GET':
        return render_template('review.html')

@app.route('/confirmation/', methods=['POST', 'GET'])
def confirmation():
    if request.method=='POST':
        return render_template('confirmation.html')
    elif request.method=='GET':
        return 'Please place an order'

app.run(debug=True)