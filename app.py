import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('Output.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    sum = 0
    for i in int_features:
        sum += i
    if sum >= 15:
        a = 'You are Eligible'
    else:
        a = 'You are not Eligible'    
    return render_template('index.html', prediction_text=' {} '.format(a))


if __name__ == "__main__":
    app.run(debug=True)
