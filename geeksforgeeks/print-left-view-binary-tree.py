class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def print_left_view(root):
    max_depth = [-1]
    preorder(root, 0, max_depth)

def preorder(root, d, max_depth):
    if root is None:
        return

    if d > max_depth[0]:
        print(root.value)
        max_depth[0] = d

    preorder(root.left, d+1, max_depth)
    preorder(root.right, d+1, max_depth)


# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.right = Node(6)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.left.right.right.right = Node(6)

print_left_view(root)
