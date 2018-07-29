import copy

class Node:
    def __init__(self, key):
        self.key = key
        self.neighbors = set()


class Path:
    def __init__(self, start):
        self.order = []
        self.visited_set = set()
        self.distance = 0
        self.add(start, 0)

    def add(self, key, distance):
        self.order.append(key)
        self.visited_set.add(key)
        self.distance += distance

    def last(self):
        return self.order[-1]

    def has_visited(self, key):
        return key in self.visited_set


class Graph:
    def __init__(self):
        self._edges = {}

    def insert_node(self, key):
        self._edges[key] = set()

    def insert_edge(self, key1, key2, distance):
        self._edges[key1].add((key2, distance))
        self._edges[key2].add((key1, distance))

    def find_shortest_path(self, from_key, to_key):
        paths = [Path(from_key)]
        reached_paths = []

        while len(paths) > 0:
            new_paths = []
            for path in paths:
                last_key = path.last()
                for key, distance in self._edges[last_key]:
                    new_path = copy.deepcopy(path)
                    if not new_path.has_visited(key): # O(1)
                        new_path.add(key, distance)
                        new_paths.append(new_path)
                        if key == to_key:
                            reached_paths.append(new_path)
            paths = new_paths

        shortest_distance = None
        shortest_paths = []
        for path in reached_paths:
            if not shortest_distance:
                shortest_distance = path.distance
                shortest_paths.append(path)
            elif shortest_distance == path.distance:
                shortest_paths.append(path)
            elif shortest_distance > path.distance:
                shortest_distance = path.distance
                shortest_paths = [path]
        return shortest_distance, [path.order for path in shortest_paths]


g = Graph()
g.insert_node(1)
g.insert_node(2)
g.insert_node(3)
g.insert_node(4)
g.insert_node(5)
g.insert_edge(1, 2, 3)
g.insert_edge(1, 3, 5)
g.insert_edge(2, 3, 1)
g.insert_edge(2, 5, 20)
g.insert_edge(3, 4, 3)
g.insert_edge(4, 5, 10)

shortest_distance, paths = g.find_shortest_path(1, 5)
print('Shortest distance', shortest_distance)
print('Shortest paths', paths)
