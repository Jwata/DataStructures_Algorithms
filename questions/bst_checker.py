class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def is_binary_search_tree(root):

    nodes = [(root, None, None)]

    while len(nodes) > 0:
        current, min_value, max_value = nodes.pop()
        # print("current value {} should be > {} and < {}".format(current.value, min_value, max_value))

        if min_value and current.value <= min_value:
            return False
        if max_value and current.value >= max_value:
            return False

        if current.left:
            node = (current.left, min_value, current.value)
            nodes.append(node)
        if current.right:
            node = (current.right, current.value, max_value)
            nodes.append(node)

    return True

# depath 0
root = BinaryTreeNode(5)

# depath 1
root.insert_left(3)
root.insert_right(6)

# depath 2
root.left.insert_left(2)
root.left.insert_right(4)
root.right.insert_right(7)

print(is_binary_search_tree(root)) # should be True

# depath 0
root = BinaryTreeNode(5)

# depath 1
root.insert_left(3)
root.insert_right(6)

# depath 2
root.left.insert_left(2)
root.left.insert_right(6)
root.right.insert_right(7)

print(is_binary_search_tree(root)) # should be False
