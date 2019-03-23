class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bst(root):
    level = 1
    buf = [(root, level)]

    prev_level = level
    while buf:
        node, level = buf.pop(0)
        if level != prev_level:
            print("")
        print(node.value, end=" ")
        prev_level = level
        
        if node.left:
            buf.append((node.left, level+1))
        if node.right:
            buf.append((node.right, level+1))

def bst_single_queue(root):
    level = 1
    buf = [root, None]

    while len(buf) > 1:
        node = buf.pop(0)
        if node is None:
            print("")
            buf.append(None)
            continue

        print(node.value, end=" ")

        if node.left:
            buf.append(node.left)
        if node.right:
            buf.append(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

bst_single_queue(root)
