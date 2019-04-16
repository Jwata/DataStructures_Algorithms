from collections import deque

class SocialGraph:
    def __init__(self, n):
        self.edges = [[] for _ in range(n)]

    def add_connection(self, i, j):
        self.edges[i].append(j)
        self.edges[j].append(i)

    def bidirectional_bfs(self, source, dest):
        i = source
        j = dest
        q1 = deque()
        q2 = deque()
        visited1 = {}
        visited2 = {}

        q1.append(source)
        visited1[source] = None
        q2.append(dest)
        visited2[dest] = None

        while len(q1) > 0 and len(q2) > 0:
            if len(q1) > 0:
                c = self.bfs(q1, visited1, visited2)
                if c:
                    return retrieve_path(c, visited1, visited2)

            if len(q2) > 0:
                c = self.bfs(q2, visited2, visited1)
                if c:
                    return retrieve_path(c, visited1, visited2)

    def bfs(self, q, v1, v2):
        cur = q.popleft()
        if cur in v2:
            return cur

        for e in self.edges[cur]:
            if not e in v1:
                v1[e] = cur
                q.append(e)


def retrieve_path(c, visited1, visited2):
    path = [c]
    c1 = c
    c2 = c

    while c1 is not None:
        c1 = visited1[c1]
        if c1 is not None:
            path = [c1] + path

    while c2 is not None:
        c2 = visited2[c2]
        if c2 is not None:
            path.append(c2)

    return path


g = SocialGraph(15)
g.add_connection(0, 4)
g.add_connection(1, 4)
g.add_connection(2, 5)
g.add_connection(3, 5)
g.add_connection(4, 6)
g.add_connection(5, 6)
g.add_connection(6, 7)
g.add_connection(7, 8)
g.add_connection(8, 9)
g.add_connection(8, 10)
g.add_connection(9, 11)
g.add_connection(9, 12)
g.add_connection(10, 13)
g.add_connection(10, 14)

source = 0
dest = 14
path = g.bidirectional_bfs(source, dest)
print(path)
