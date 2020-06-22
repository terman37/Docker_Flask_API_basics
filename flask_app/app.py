from flask import Flask, request
import pickle
import numpy as np

server = Flask(__name__)

model = pickle.load(open('../training/pipe.pkl', 'rb'))


@server.route('/')
def hello_world():
	
    return 'hello world'


@server.route('/predict/', methods=['GET', 'POST'])
def predict():

    # Get request argument
    xget = request.args.get("x")
    try:
    	xget = float(xget)
    except TypeError:
    	print("Bad conversion type")

    # Predict
    ypred = pipe.predict(x)[0]

    # display massage
    print("x= %.2f --> y= %.2f" % (xget, ypred))
    return str(ypred)
