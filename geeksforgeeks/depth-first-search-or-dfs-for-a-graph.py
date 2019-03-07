from collections import defaultdict


class Graph:
    def __init__(self):
        self.edges = defaultdict(set)

    def add_edge(self, from_node, to_node):
        self.edges[from_node].add(to_node)

    def dfs_print(self, start_node):
        buf = [start_node]
        visited = set()

        while len(buf) > 0:
            cur = buf.pop()

            if cur is not visited:
                print(cur)
                visited.add(cur)

            for e in self.edges[cur]:
                if not e in visited:
                    buf.append(e)

    def dfs_recursive_print(self, start_node):
        visited = set()

        self._dfs_helper(start_node, None, visited)

    def _dfs_helper(self, node, prev, visited):
        visited.add(node)
        print(node)

        for e in self.edges[node]:
            if not e in visited:
                self._dfs_helper(e, node, visited)


print("Case 1")
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("iterative dfs")
g.dfs_print(2)
print("recursion dfs")
g.dfs_recursive_print(2)

print("Case 2")
g = Graph()
g.add_edge(1, 0)
g.add_edge(0, 2)
g.add_edge(2, 1)
g.add_edge(0, 3)
g.add_edge(1, 4)

print("iterative dfs")
g.dfs_print(0)
print("recursion dfs")
g.dfs_recursive_print(0)
