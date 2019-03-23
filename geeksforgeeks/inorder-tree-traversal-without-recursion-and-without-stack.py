class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder_traverse(root):
    cur = root
    while cur:
        if not cur.left:
            print(cur.value)
            cur = cur.right
        else:
            pre = cur.left
            while pre.right and pre.right != cur:
                pre = pre.right
            if pre.right is None:
                pre.right = cur
                cur = cur.left
            else:
                pre.right = None
                print(cur.value)
                cur = cur.right


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)

inorder_traverse(root)
