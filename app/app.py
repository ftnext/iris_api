from flask import Flask
from flask import jsonify
from flask import request
import numpy as np
from sklearn.externals import joblib

IRIS_KIND = ['setosa', 'versicolor', 'virginica']

app = Flask(__name__)
sc = joblib.load('sc_iris_petal.pkl')
ppn = joblib.load('ppn_iris.pkl')

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/predict', methods=['POST'])
def predict():
    input_ = request.get_json()
    length = float(input_['length'])
    width = float(input_['width'])
    input_std = sc.transform(np.array([[length, width]]))
    prediction = ppn.predict(input_std)
    response = jsonify(
        {'prediction': IRIS_KIND[int(prediction[0])]})
    response.status_code = 200
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0')
