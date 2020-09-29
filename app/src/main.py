from flask import Flask, request, jsonify
import pickle
import numpy as np
import time

myapi = Flask(__name__)
model = pickle.load(open('./src/model.pkl', 'rb'))


def dumb(i):
    return i * 2


@myapi.route('/')
def hello_world():
    return 'hello world'


@myapi.route('/predict/', methods=['GET', 'POST'])
def predictln():
    # Get request argument
    t1 = time.time()
    x_get = request.args.get("x")
    try:
        x_full = np.array(float(x_get)).reshape(-1, 1)
    except Exception as e:
        print("Bad conversion type")
        result = e.args[0]
    else:
        # Predict
        y_pred = model.predict(x_full)[0]
        # display message
        print("x= --> %.2f y= %.2f" % (x_full,  y_pred))
        t2 = time.time()
        result = jsonify(pred=y_pred, duration=t2-t1)

    return result


if __name__ == "__main__":
    myapi.run()
