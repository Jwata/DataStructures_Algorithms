class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def flatten(root):
    return flatten1(root, [None])
    # return flatten2(root)

def flatten1(root, prev):
    if root is None:
        return

    flatten1(root.right, prev)
    flatten1(root.left, prev)
    root.right = prev[0]
    root.left = None
    prev[0] = root
    return prev[0]

def flatten2(root):
    if root is None:
        return

    tmp_right = flatten2(root.right)
    root.right = flatten2(root.left)
    root.left = None

    tail = root
    while tail.right:
        tail = tail.right
    tail.right = tmp_right

    return root

def print_list(root):
    if root is None:
        return
    print(root.value)
    print_list(root.right)


# root = Node(1)
# root.left = Node(2)
# root.right = Node(5)
# root.left.left = Node(3)
# root.left.right = Node(4)
# root.right.right = Node(6)

root = Node(1)
root.left = Node(3)
root.right = Node(4)
root.right.left = Node(2)
root.right.left.right = Node(5)

root = flatten(root)
print_list(root)
