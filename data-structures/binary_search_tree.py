class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        root = Node(value)
    elif value > root.value:
        if root.right:
            insert(root.right, value)
        else:
            root.right = Node(value)
    elif value < root.value:
        if root.left:
            insert(root.left, value)
        else:
            root.left = Node(value)

    return root

def minNode(root):
    if root.left is None:
        return root
    else:
        return minNode(root.left)

def delete(root, value):
    if root is None:
        return root

    if value < root.value:
        root.left = delete(root.left, value)
    elif value > root.value:
        root.right = delete(root.right, value)
    else:
        if root.left is None:
            successor = root.right
            root = None
            return successor
        elif root.right is None:
            successor = root.left
            root = None
            return successor

        successor = minNode(root.right)
        root.value = successor.value
        root.right = delete(root.right, successor.value)

    return root

def inorderPrint(root):
    if root is None:
        return
    inorderPrint(root.left)
    print(root.value)
    inorderPrint(root.right)

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

delete(root, 60)

inorderPrint(root)
