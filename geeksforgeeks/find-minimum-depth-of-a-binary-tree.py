class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.left == None and self.right == None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

def min_depth(root):
    q = [(1, root)]

    cur =None
    while len(q) > 0:
        d, cur = q.pop(0)

        if cur.is_leaf():
            return d

        if cur.left is not None:
            q.append((d+1, cur.left))
        if cur.right is not None:
            q.append((d+1, cur.right))

print(min_depth(root))
