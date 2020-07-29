from flask import Flask, request, jsonify
import pickle
import time

# from custlib.custom_transformer import custom_preproc,  custom_preproc_ln

server = Flask(__name__)
pipeln = pickle.load(open('../training/model.pkl', 'rb'))


@server.route('/')
def hello_world():
    return 'hello world'


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
