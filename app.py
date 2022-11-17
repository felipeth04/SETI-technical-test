from flask import Flask, jsonify
from model_node import *

app = Flask(__name__)


@app.route('/')
def hello_seti():
    return "Hello SETI, I'm Juan Felipe Tamayo and I really enjoyed this technical test"


@app.route('/getCommonAncestor')
def get_common_ancestor():
    root = create_tree(70, 49, 37, 54, 84, 78, 85, 22, 40, 51, 76, 80)
    return jsonify(common_node(root, 76, 85))


if __name__ == '__main__':
    app.run()
