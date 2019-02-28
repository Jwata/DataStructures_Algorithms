class Node:
    def __init__(self, value):
        self.value = value
        self.nodes = []

a = Node(2)
b = Node(0)
c = Node(1)
d = Node(3)

a.nodes.append(b)
a.nodes.append(d)
b.nodes.append(a)
b.nodes.append(c)
c.nodes.append(a)
d.nodes.append(d)

def bfs(s):
    buf = [s]
    visited = set([s.value])

    while len(buf) > 0:
        cur = buf.pop(0)
        print(cur.value)

        for n in cur.nodes:
            if not n.value in visited:
                buf.append(n)
                visited.add(n.value)

bfs(a)
