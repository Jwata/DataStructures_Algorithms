from heapq import *


class Graph:
    def __init__(self):
        self._edges = {}

    def insert_node(self, node):
        self._edges[node] = {}

    def insert_edge(self, node1, node2, distance):
        self._edges[node1][node2] = distance
        self._edges[node2][node1] = distance

    # dijkstra algorithm
    def find_shortest_path(self, from_node, to_node):
        dist_map = {from_node: 0}
        pred_map = {}
        finalized_nodes = set()
        queue = [(0, from_node)]

        while not to_node in finalized_nodes:
            dist_from_source, node = heappop(queue)
            if dist_map[node] < dist_from_source:
                continue

            print('Current {}, Distance from source {}'.format(node, dist_from_source))
            finalized_nodes.add(node)

            for adj_node, dist_to_adj in self._edges[node].items():
                if adj_node in finalized_nodes:
                    continue
                dist_to_adj_from_source = dist_from_source + dist_to_adj
                if not adj_node in dist_map or dist_map[adj_node] > dist_to_adj_from_source:
                    dist_map[adj_node] = dist_to_adj_from_source
                    pred_map[adj_node] = node
                    heappush(queue, (dist_to_adj_from_source, adj_node))
            print('Queue', queue)

        shortest_dist = dist_map[to_node]

        node = to_node
        shortest_path = [to_node]
        while True:
            pred = pred_map[node]
            shortest_path = [pred] + shortest_path
            if pred == from_node:
                break
            else:
                node = pred

        return shortest_dist, shortest_path


g = Graph()
g.insert_node('u')
g.insert_node('d')
g.insert_node('a')
g.insert_node('c')
g.insert_node('i')
g.insert_node('t')
g.insert_node('y')
g.insert_edge('u', 'a', 4)
g.insert_edge('u', 'c', 6)
g.insert_edge('u', 'd', 3)
g.insert_edge('d', 'c', 4)
g.insert_edge('a', 'i', 7)
g.insert_edge('c', 'i', 4)
g.insert_edge('c', 't', 5)
g.insert_edge('i', 'y', 4)
g.insert_edge('t', 'y', 5)

dist, path = g.find_shortest_path('u', 'y')
print('Shortest distance', dist)
print('Shortest paths', path)
