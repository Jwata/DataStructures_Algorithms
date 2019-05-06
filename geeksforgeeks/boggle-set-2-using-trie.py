from collections import defaultdict

class Trie:
    class Node:
        def __init__(self):
            self.children = defaultdict(lambda:None)
            self.end = False

        def next(self, c):
            if self.children[c] is None:
                self.children[c] = self.Node()
            return self.children[c]

    def __init__(self):
        self.root = self.Node()

    def insert(self, word):
        cur = self.root

        n = len(word)
        for i in range(n):
            c = word[i]
            cur = cur.next(c)

        cur.end = True

class Boggle:
    def __init__(self, boggle, n, m):
        self.n = n
        self.m = m
        self.boggle = boggle

    def find_words(self, D):
        # build trie
        t = Trie()
        for w in D:
            t.insert(w)

        words = []
        for i in range(self.n):
            for j in range(self.m):
                words += self.dfs(i, j, t)
        return words

    def dfs(self, i, j, trie):
        visited = [[False for _ in range(self.m)] for _ in range(self.n)]

        words = []
        prefix = ''
        self.dfs_helper(i, j, visited, prefix, words, trie.root)
        return words

    def dfs_helper(self, i, j, visited, prefix, words, trie_node):
        if visited[i][j]:
            return

        c = self.boggle[i][j]
        if trie_node.children[c] is None:
            return

        visited[i][j] = True
        prefix += c
        trie_node = trie_node.children[c]

        if trie_node.end:
            words.append(prefix)

        for adj_i, adj_j in self.get_adjacents(i, j):
            self.dfs_helper(adj_i, adj_j, visited, prefix, words, trie_node)

        visited[i][j] = False

    def get_adjacents(self, i, j):
        nodes = []

        for _i in range(max(i-1, 0), min(i+2, self.n)):
            for _j in range(max(j-1, 0), min(j+2, self.m)):
                if not (_i == i and _j == j):
                    nodes.append((_i, _j))

        return nodes

n = 3
m = 3
boggle = [['G', 'I', 'Z'],\
          ['U', 'E', 'K'],\
          ['Q', 'S', 'E']]
D = ['GEEKS', 'FOR', 'QUIZ', 'GO']

b = Boggle(boggle, n, m)
words = b.find_words(D)
print(words)
