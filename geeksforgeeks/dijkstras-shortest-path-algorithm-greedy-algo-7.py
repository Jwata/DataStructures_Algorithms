
INT_MAX = 2 ** 31 - 1

class Graph:
    def __init__(self, num_nodes):
        self.edges = [[] for _ in range(num_nodes)]

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append((to_node, weight))
        self.edges[to_node].append((from_node, weight))

    def dijkstra(self, start, end):
        n = len(self.edges)
        distances =[(INT_MAX, None)] * n
        nodes = set(range(n))
        spt = [None] * n

        distances[start] = (0, None)

        while len(nodes) > 0:
            node = get_next_node(distances, nodes)
            d, prev_node = distances[node]

            nodes.remove(node)
            spt[node] = prev_node

            if node == end:
                break

            # update distances of adjacent nodes
            for to_node, weight in self.edges[node]:
                if d + weight < distances[to_node][0]:
                    distances[to_node] = (d+weight, node)

        distance = distances[end][0]
        path = construct_path_from_spt(spt, end)
        return distance, path


def get_next_node(distances, nodes):
    next_node = None
    for node in nodes:
        if next_node is None or distances[node][0] < distances[next_node][0]:
            next_node = node
    return next_node

def construct_path_from_spt(spt, end):
    path = [end]
    node = end

    while spt[node] is not None:
        next_node = spt[node]
        path.append(next_node)
        node = next_node

    path.reverse()
    return path


num_nodes = 9
g = Graph(num_nodes)
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
print(g.dijkstra(0, 4))
