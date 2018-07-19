class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)
            # TODO: rebarance

    def _insert(self, node, value):
        if value <= node.value:
            if node.left:
                self._insert(node.left, value)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self._insert(node.right, value)
            else:
                node.right = Node(value)

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if not node:
            return False
        elif node.value == value:
            return True
        elif value < node.value:
            if node.left:
                return self._search(node.left, value)
            else:
                return False
        elif value > node.value:
            if node.right:
                return self._search(node.right, value)
            else:
                return False

    def delete(self, value):
        pass

    def traverse(self):
        return self.preorder_traverse(self.root, [])

    def preorder_traverse(self, start, traversal):
        if not start:
            return traversal
        traversal.append(start.value)
        if start.left:
            traversal = self.preorder_traverse(start.left, traversal)
        if start.right:
            traversal = self.preorder_traverse(start.right, traversal)
        return traversal


tree = RedBlackTree()
tree.insert(1)
tree.insert(10)
tree.insert(7)
tree.insert(5)

traversal = tree.traverse()
print(traversal)

print(tree.search(4))
print(tree.search(5))

import ipdb; ipdb.set_trace()
