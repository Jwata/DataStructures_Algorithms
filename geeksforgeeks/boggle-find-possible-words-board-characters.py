class Boggle:
    def __init__(self, boggle, n, m):
        self.n = n
        self.m = m
        self.boggle = boggle

    def find_words(self, D):
        words = []

        for i in range(self.n):
            for j in range(self.m):
                words += self.dfs(i, j, D)

        return words

    def dfs(self, i, j, D):
        visited = [[False for _ in range(m)] for _ in range(n)]
        prefix = ''
        words = []
        self.dfs_helper(i, j, visited, prefix, words, D)
        return words

    def dfs_helper(self, i, j, visited, prefix, words, D):
        if visited[i][j]:
            return
        visited[i][j] = True
        prefix += self.boggle[i][j]
        if prefix in D:
            words.append(prefix)

        for adj_i, adj_j in self.get_adjacents(i, j):
            self.dfs_helper(adj_i, adj_j, visited, prefix, words, D)

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
