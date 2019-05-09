class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None

def connect_nodes_at_same_level(root):
    q = [(root, 0)]
    prev_d = -1
    prev = None

    while len(q) > 0:
        cur, d = q.pop(0)
        if d > prev_d:
            prev = None
        if prev:
            prev.next = cur
        if cur.left:
            q.append((cur.left, d+1))
        if cur.right:
            q.append((cur.right, d+1))
        prev = cur
        prev_d = d

    return root

root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.right = Node('F')

connect_nodes_at_same_level(root)
