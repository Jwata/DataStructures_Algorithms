from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def print_top_view(root):
    q = deque()
    q.append((root, 0))
    view_map = {}

    hd_min = 0
    hd_max = 0

    while len(q) > 0: # O(n)
        node, hd = q.popleft()
        hd_min = min(hd, hd_min)
        hd_max = max(hd, hd_max)

        if not hd in view_map:
            view_map[hd] = node.value

        if node.left:
            q.append((node.left, hd-1))
        if node.right:
            q.append((node.right, hd+1))

    for i in range(hd_min, hd_max+1): #O(n)
        print(view_map[i])

print("Tree 1")
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print_top_view(root)

print("Tree 2")
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.left.right.right.right = Node(6)
print_top_view(root)
