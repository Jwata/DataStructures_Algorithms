# this is wip to improve using queue.replace

from priority_queue import PriorityQueue

class Graph:
    def __init__(self, V):
        self.V = V
        self.edges = [[] for _ in range(V)]

    def add_edge(self, i, j, w):
        self.edges[i].append((j, w))
        self.edges[j].append((i, w))

    def find_mst(self):
        parent = {}
        mst_set = set()
        queue = PriorityQueue() # keep edges to explore

        # init with edges of node 0
        queue.arr.append((0, 0))
        queue.pos[0] = 0

        while not queue.empty():
            w, i = queue.pop()
            mst_set.add(i)

            print(i, queue.pos)
            for j, w in self.edges[i]:
                if j not in mst_set:
                    p = queue.priority(j)
                    if p is None:
                        queue.push(w, j)
                        parent[j] = i
                    elif p > w:
                        queue.replace(w, j)
                        parent[j] = i

        return parent


g = Graph(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 7, 8)
g.add_edge(1, 2, 8)
g.add_edge(1, 7, 11)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 14)
g.add_edge(4, 5, 10)
g.add_edge(5, 6, 2)
g.add_edge(6, 7, 1)
g.add_edge(6, 8, 6)
g.add_edge(7, 8, 7)
g.add_edge(2, 3, 7)
g.add_edge(2, 8, 2)
g.add_edge(2, 5, 4)

print(g.find_mst())
