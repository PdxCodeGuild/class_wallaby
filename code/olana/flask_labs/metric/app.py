from flask import Flask, render_template,request

app = Flask(__name__)

meters_dict = {
    'ft':.3048,
    'mi':1609.34,
    'm':1,
    'km':1000,
    'y':0.9144,
    'in':0.0254 
}

@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        metric = request.form.get("metric")
        print(metric)
        # distance = int(metric)
        # conversion = meters_dict[metric]
        # calculate = distance * conversion
        # print(calculate)








        return render_template("index.html", metric=metric)
    elif request.method == "GET":
        return render_template("index.html")