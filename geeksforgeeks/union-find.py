class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = []

    def add_edge(self, i, j):
        self.edges.append((i, j))

def has_cycle(graph):
    parents = [-1 for _ in range(graph.n)]

    def find(i):
        if parents[i] == -1:
            return i
        return find(parents[i])

    def union(x, y):
        parents[x] = y

    for i, j in graph.edges:
        x = find(i)
        y = find(j)
        if x == y:
            return True
        union(x, y)

    return False


g = Graph(5)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(1,4)
g.add_edge(3,4)

print(has_cycle(g)) # True
