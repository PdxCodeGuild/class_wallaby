from flask import Flask, render_template,request

app = Flask(__name__)

#Rot code
import string

@app.route("/", methods=["GET","POST"])
def homepage():
    if request.method == "POST":
        initial = request.form.get("initial")
        english_alphabet = string.ascii_lowercase  
        text = initial.lower()
        rot_13_message = ''
        
        for character in text:
            if character.isalpha():
                rot_13_message += english_alphabet[(english_alphabet.index(character) + 13) % 26]
            else:
                rot_13_message += character
        return render_template("index.html",rot_13_message=rot_13_message)
    elif request.method == "GET":
        return render_template("index.html")



