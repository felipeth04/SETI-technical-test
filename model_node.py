class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_node(self, root, node):
        if root is None:
            root = node
        else:
            if root.data < node.data:
                if root.right is None:
                    root.right = node
                else:
                    self.add_node(root.right, node)
            else:
                if root.left is None:
                    root.left = node
                else:
                    self.add_node(root.left, node)


def search_node(root, data):
    if root is None:
        message = "The node"+" "+str(data)+" "+"you searched doesn't exits"
    elif root.data == data:
        message = "The node"+" "+str(data)+" "+"you searched currently exits"
    elif data < root.data:
        message = search_node(root.left, data)
    elif data > root.data:
        message = search_node(root.right, data)

    return message


def search_common_node(root, x, y):
    if root is None:
        return None

    if root.data > max(x, y):
        return search_common_node(root.left, x, y)

    elif root.data < min(x, y):
        return search_common_node(root.right, x, y)

    return root.data


def common_node(root, x, y):
    if not root or not search_node(root, x) or not search_node(root, y):
        response = {"message": "the common node does not exist..."}
        return response

    common_search = search_common_node(root, x, y)

    if common_search:
        response = {"The common node is:": common_search}
        return response
    else:
        response = {"message": "the common node does not exist..."}
        return response
