class Graph:
    def __init__(self, n_v):
        self.n_v = n_v
        self.edges = []

    def add_edge(self, i, j, w):
        self.edges.append((w, i, j))

    # n log n
    def sort_edges(self):
        return sorted(self.edges)

    def find_mst(self):
        mst = []

        parents = [-1 for _ in range(self.n_v)]

        def find(i):
            if parents[i] == -1:
                return i
            return find(parents[i])

        def union(x, y):
            parents[x] = y

        for w, i, j in self.sort_edges():
            x = find(i)
            y = find(j)
            if  x != y:
                mst.append((w, i, j))
                union(x, y)
            if len(mst) == self.n_v - 1:
                break

        return mst


g = Graph(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 7, 8)
g.add_edge(1, 2, 8)
g.add_edge(1, 7, 11)
g.add_edge(2, 3, 7)
g.add_edge(2, 5, 4)
g.add_edge(2, 8, 2)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 14)
g.add_edge(4, 5, 10)
g.add_edge(5, 6, 2)
g.add_edge(6, 7, 1)
g.add_edge(6, 8, 6)
g.add_edge(7, 8, 7)

print(g.find_mst())
