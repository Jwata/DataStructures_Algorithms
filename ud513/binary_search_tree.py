class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.preorder_insert(self.root, new_val)
    
    def preorder_insert(self, node, new_val):
        if node.value == new_val:
            # Should we raise an error?
            return
        elif new_val < node.value:
            if node.left:
                self.preorder_insert(node.left, new_val)
            else:
                node.left = Node(new_val)
        elif new_val > node.value:
            if node.right:
                self.preorder_insert(node.right, new_val)
            else:
                node.right = Node(new_val)

    def search(self, find_val):
        return self.preorder_search(self.root, find_val)
        
    def preorder_search(self, node, find_val):
        if not node:
            return False
        elif node.value == find_val:
            return True
        elif find_val < node.value:
            return self.preorder_search(node.left, find_val)
        elif node.value < find_val:
            return self.preorder_search(node.right, find_val)

    def traverse(self):
        return self.preorder_traverse(self.root, [])

    def preorder_traverse(self, start, traversal):
        traversal.append(start.value)
        if start.left:
            traversal = self.preorder_traverse(start.left, traversal)
        if start.right:
            traversal = self.preorder_traverse(start.right, traversal)
        return traversal

    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# print(tree.traverse())

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
