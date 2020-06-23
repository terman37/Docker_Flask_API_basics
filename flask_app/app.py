from flask import Flask, request, jsonify
import pickle
import numpy as np
import json
import time

from custlib.custom_transformer import custom_preproc,  custom_preproc_ln

server = Flask(__name__)
pipe = pickle.load(open('../digits_training/model.pkl', 'rb'))
pipeln = pickle.load(open('../training/model.pkl', 'rb'))

@server.route('/')
def hello_world():
    return 'hello world'


@server.route('/predict/', methods=['GET', 'POST'])
def predict():
    # Get request argument
    t1 = time.time()
    x_get = request.args.get("json")
    try:
        x_full = json.loads(x_get)
    except Exception as e:
        print("Bad conversion type")
        result = e.args[0]
    else:
        # Predict
        y_pred = int(pipe.predict(x_full['image'])[0])
        # display message
        print("%s x= --> y= %.2f" % (x_full['author'],  y_pred))
        t2 = time.time()
        result = jsonify(pred=y_pred, duration=t2-t1)

    return result


@server.route('/predictln/', methods=['GET', 'POST'])
def predictln():
    # Get request argument
    t1 = time.time()
    x_get = request.args.get("x")
    try:
        x_full = float(x_get)
    except Exception as e:
        print("Bad conversion type")
        result = e.args[0]
    else:
        # Predict
        y_pred = pipeln.predict(x_full)[0]
        # display message
        print("x= --> %.2f y= %.2f" % (x_full,  y_pred))
        t2 = time.time()
        result = jsonify(pred=y_pred, duration=t2-t1)

    return result