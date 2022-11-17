from flask import Flask,jsonify
from model_node import *

app = Flask(__name__)


@app.route('/')
def hello_seti():
    return "Hello SETI, I'm Juan Felipe Tamayo and I really enjoyed this technical test"



if __name__ == '__main__':
    app.run()
