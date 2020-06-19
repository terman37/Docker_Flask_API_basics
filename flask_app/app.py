from flask import Flask, request
import pickle
import numpy as np

server = Flask(__name__)

model = pickle.load(open('../training/model.pkl', 'rb'))


@server.route('/')
def hello_world():
    return 'hello world'


@server.route('/predict/', methods=['GET', 'POST'])
def predict():

    xget = request.args.get("x")
    print(xget)
    xget = float(xget)
    x = np.array([[xget]])
    ypred = model.predict(x)
    return str(ypred)
