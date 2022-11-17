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