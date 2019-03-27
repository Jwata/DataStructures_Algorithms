class Trie:
    class Node:
        def __init__(self):
            self.children = [None, None] 

    def __init__(self):
        self.root = self.Node()

    def insert(self, arr):
        cur = self.root

        for i in range(n):
            visited = False
            if cur.children[arr[i]]:
                visited = True
            else:
                cur.children[arr[i]] = self.Node()

            cur = cur.children[arr[i]]

        return visited


t = Trie()


print("First matrix")
M = [[0, 1, 0], [1, 0, 0], [0, 1, 0]]
n = 3

for i in range(n):
    row = M[i]
    if t.insert(row):
        print("duplicated row %d" % i)

print("Second matrix")
M = [[1, 1, 0, 1, 0, 1], \
     [0, 0, 1, 0, 0, 1], \
     [1, 0, 1, 1, 0, 0], \
     [1, 1, 0, 1, 0, 1], \
     [0, 0, 1, 0, 0, 1], \
     [0, 0, 1, 0, 0, 1]]
n = 6

for i in range(n):
    row = M[i]
    if t.insert(row):
        print("duplicated row %d" % i)
