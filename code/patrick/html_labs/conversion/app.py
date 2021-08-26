from flask import Flask, render_template, request, redirect
import numpy as np
import subprocess
from flask import (
    Blueprint, flash, Flask, g, redirect, render_template, request, session, url_for, request, redirect
)
import requests
from datetime import datetime
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():   
    return render_template('convert.html', )

@app.route('/converts/', methods=['POST', 'GET'])
def converts():
    if request.method == 'POST':
       
        distance = int(request.form['distance'])
        input_units = request.form['Input Units']
        output_units = request.form['Output Units']
        def conversion(distance, input_units, output_units):
            data = np.array([[0.3048], [1609.34], [1], [1000]])
            np.set_printoptions(suppress=True)
            if input_units == 'ft':
                meters = data[0]*distance
            elif input_units == 'mi':
                meters = data[1]*distance
            elif input_units == 'm':
                meters = data[2]*distance
            elif input_units == 'km':
                meters = data[3]*distance
            
            if output_units == 'ft':
                meters = meters / data[0]   
            elif output_units == 'mi':
                meters = meters / data[1] 
            elif output_units == 'm':
                meters = meters / data[2]
            elif output_units == 'km':
                meters = meters / data[3]
            # meters = np.round(meters, 0)
            # np.set_printoptions(precision=0)
            if meters[0] >= 1:
                meters = round(meters[0], 0)
            else:
                meters = round(meters[0], 4)
            return meters
        conversion_1 = conversion(distance, input_units, output_units)
        print(conversion_1)
        # while True: 
        #     try:
        #         # distance = int(input('What is the distance? '))
        #         # input_units = (input('What are the input units? ').lower())
        #         # output_units = (input('What are the output units? ').lower())

        #         conversion_1 = conversion(distance, input_units, output_units)
        #         print(f'The distance of {distance}{input_units} is equal to {conversion_1}{output_units}')
        #         again = input('again?: ').lower()
        #         if again == 'y' or again == 'yes':
        #             continue
        #         else:
        #             break

        #     except ValueError:
        #         print("enter valid entry")
        #         continue

        return render_template('results.html', conversion_1=conversion_1)

if __name__ == "__main__":
    app.run(debug=True)