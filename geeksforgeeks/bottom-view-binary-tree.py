from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def print_bottom_view(self):
        if not self.root:
            return

        q = deque()
        q.append((self.root, 0))

        bottom_nodes = {}

        while len(q) > 0:
            node, dist = q.popleft()
            bottom_nodes[dist] = node

            if node.left:
                q.append((node.left, dist-1))
            if node.right:
                q.append((node.right, dist+1))

        bottom_view = []
        for k, n in bottom_nodes.items():
            bottom_view.append((k, n))

        bottom_view.sort()
        for _, n in bottom_view:
            print(n.value)


t = Tree()
t.root = Node(20)
t.root.left = Node(8)
t.root.left.left = Node(5)
t.root.left.right = Node(3)
t.root.left.right.left = Node(10)
t.root.left.right.right = Node(14)
t.root.right = Node(22)
t.root.right.left = Node(4)
t.root.right.right = Node(25)

t.print_bottom_view()
