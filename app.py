from flask import Flask, jsonify
from model_node import *

app = Flask(__name__)


@app.route('/')
def hello_seti():
    return "Hello SETI, I'm Juan Felipe Tamayo and I really enjoyed this technical test"


@app.route('/getCommonAncestor/<int:node_one>/<int:node_two>')
def get_common_ancestor(node_one, node_two):
    root = create_tree(70, 49, 37, 54, 84, 78, 85, 22, 40, 51, 76, 80)
    if not search_node(root, node_one) and not search_node(root, node_two):
        response = {"message": "The params doesn't exist in the binary tree..."}
        return response
    return jsonify(common_node(root, node_one, node_two))


@app.route('/getNode/<int:data>')
def search_individual_node(data):
    root = create_tree(70, 49, 37, 54, 84, 78, 85, 22, 40, 51, 76, 80)
    if search_node(root,data) == True:
        return jsonify({"message": "The node you searched for currently exists"})
    else:
        return jsonify({"message": "The node you searched for doesn't exists"})


if __name__ == '__main__':
    app.run()
