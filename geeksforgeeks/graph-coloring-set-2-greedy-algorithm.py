class Graph:
    def __init__(self, V):
        self.V = V
        self.edges = [[] for _ in range(V)]

    def add_edge(self, i, j):
        self.edges[i].append(j)
        self.edges[j].append(i)

    def color(self):
        max_color = 0
        colors = [None for _ in range(self.V)]

        for v in range(self.V):
            adj_colors = set()
            for adj in self.edges[v]:
                if colors[adj]:
                    adj_colors.add(colors[adj])
            for c in range(1, self.V+1):
                if not c in adj_colors:
                    colors[v] = c
                    max_color = max(max_color, c)
                    break

        return colors, max_color

g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)

print(g.color())
