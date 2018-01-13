class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add_to_left(self, value):
        self.left = BinaryTreeNode(value)

    def add_to_right(self, value):
        self.right = BinaryTreeNode(value)
