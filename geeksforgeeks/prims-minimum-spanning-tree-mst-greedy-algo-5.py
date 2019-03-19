from priority_queue import PriorityQueue

class Graph:
    def __init__(self, V):
        self.V = V
        self.edges = [[None for _ in range(V)] for _ in range(V)]

    def add_edge(self, i, j, w):
        self.edges[i][j] = w
        self.edges[j][i] = w

    def find_mst(self):
        mst_edges = [] # (from, to, weight)
        mst_set = set()
        queue = PriorityQueue() # keep edges to explore

        def add_edges(i): # O(E)
            for j, w in enumerate(self.edges[i]):
                if w is not None:
                    queue.push(w, (i, j))

        def pop_edge(): # O(1)
            return queue.pop()

        # init with edges of node 0
        add_edges(0)

        while not queue.empty():
            w, (n1, n2) = pop_edge() # O(1)

            # will make cycle?
            if n1 in mst_set and n2 in mst_set:
                continue

            # add candidate edges
            if n1 not in mst_set:
                add_edges(n1)
                mst_set.add(n1)
            if n2 not in mst_set:
                add_edges(n2)
                mst_set.add(n2)

            # add to mst
            mst_edges.append((w, n1, n2))

        return mst_edges


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

mst_edges = g.find_mst()
print(mst_edges)
