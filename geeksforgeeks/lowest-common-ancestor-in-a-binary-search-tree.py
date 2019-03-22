class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_lca(root, a, b):
    cur = root
    while True:
        if a < cur.value and b < cur.value:
            cur = cur.left
        elif a > cur.value and b > cur.value:
            cur = cur.right
        else:
            return cur

def find_lca_recur(root, a, b):
    cur = root

    if a < cur.value and b < cur.value:
        return find_lca_recur(cur.left, a, b)
    elif a > cur.value and b > cur.value:
        return find_lca_recur(cur.right, a, b)
    else:
        return cur

root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

print(find_lca(root, 10, 14).value) # 12
print(find_lca_recur(root, 10, 14).value) # 12
