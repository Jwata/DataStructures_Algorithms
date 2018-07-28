import copy

class Node:
    def __init__(self, key):
        self.key = key
        self.neighbors = set()


class Path:
    def __init__(self, start):
        self.order = []
        self.visited_set = set()
        self.add(start)

    def add(self, key):
        self.order.append(key)
        self.visited_set.add(key)

    def last(self):
        return self.order[-1]

    def has_visited(self, key):
        return key in self.visited_set


class Graph:
    def __init__(self):
        self._node_map = {}

    def get_node(self, key):
        return self._node_map[key]

    def insert_node(self, key):
        if key in self._node_map:
            return
        node = Node(key)
        self._node_map[key] = node

    def insert_edge(self, key1, key2):
        node1 = self.get_node(key1)
        node2 = self.get_node(key2)
        node1.neighbors.add(key2)
        node2.neighbors.add(key1)

    def find_shortest_path(self, from_key, to_key):
        paths = [Path(from_key)]

        shortest_paths = []

        while len(shortest_paths) <= 0:
            new_paths = []
            for path in paths:
                last_node = self.get_node(path.last())
                for neighbor_key in last_node.neighbors:
                    new_path = copy.deepcopy(path)
                    if not new_path.has_visited(neighbor_key): # O(1)
                        new_path.add(neighbor_key)
                        new_paths.append(new_path)
                        if neighbor_key == to_key:
                            shortest_paths.append(new_path)
            paths = new_paths

        return [path.order for path in shortest_paths]


g = Graph()
g.insert_node(1)
g.insert_node(2)
g.insert_node(3)
g.insert_node(4)
g.insert_node(5)
g.insert_edge(1, 2)
g.insert_edge(1, 3)
g.insert_edge(2, 5)
g.insert_edge(3, 4)
g.insert_edge(4, 5)

paths = g.find_shortest_path(1, 5)
print(paths)
