from collections import defaultdict

class DAG:
    def __init__(self):
        self.edges = defaultdict(lambda: [])
        self.chars = set()

    def add_edge(self, i, j):
        self.edges[i].append(j)
        self.chars.add(i)
        self.chars.add(j)

    def topological_sort(self):
        stack = []
        visited = defaultdict(lambda: False)

        for c in self.chars:
            self.dfs(c, stack, visited)

        stack.reverse()
        return stack

    def dfs(self, c, stack, visited):
        if visited[c]:
            return
        visited[c] = True

        for adj in self.edges[c]:
            self.dfs(adj, stack, visited)

        stack.append(c)

def find_order(words):
    dag = DAG()

    n = len(words)
    for i in range(n-1):
        word_a = words[i]
        word_b = words[i+1]

        char_a, char_b = find_different_chars(word_a, word_b)
        if not char_a or not char_b:
            continue

        dag.add_edge(char_a, char_b)

    return dag.topological_sort()

def find_different_chars(a, b):
    na = len(a)
    nb = len(b)
    j = 0

    while j < na and j < nb:
        ca = a[j]
        cb = b[j]
        if ca == cb:
            j += 1
            continue
        return ca, cb

    return None, None

words = ['baa', 'abcd', 'abca', 'cab', 'cad']            
print(find_order(words))
