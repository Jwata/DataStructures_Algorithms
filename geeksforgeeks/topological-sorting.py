from collections import defaultdict

class DAG:
    def __init__(self, V):
        self.edges = {}
        self.V = V
        for v in range(self.V):
            self.edges[v] = []

    def add_edge(self, i, j):
        self.edges[i].append(j)

    def topological_sort(self):
        stack = []
        visited = defaultdict(lambda: False)

        for v in range(self.V):
            self.dfs(v, visited, stack)

        stack.reverse()
        return stack

    def dfs(self, v, visited, stack):
        if visited[v]:
            return

        visited[v] = True
        for i in self.edges[v]:
            self.dfs(i, visited, stack)
        stack.append(v)


dag = DAG(6)
dag.add_edge(5, 0)
dag.add_edge(5, 2)
dag.add_edge(4, 0)
dag.add_edge(4, 1)
dag.add_edge(2, 3)
dag.add_edge(3, 1)

sorted_list = dag.topological_sort()
print(sorted_list)
