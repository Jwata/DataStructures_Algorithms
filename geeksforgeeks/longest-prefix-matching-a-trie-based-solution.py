from collections import defaultdict

class Node:
    def __init__(self):
        self.children = defaultdict(lambda: None)
        self.eof = None

    def next(self, value):
        return self.children[value]

    def append(self, value):
        if self.children[value]:
            raise Exception('next node already exist')
        self.children[value] = Node()

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        n = len(word)

        node = self.root
        for i in range(n):
            c = word[i]
            if not node.next(c):
                node.append(c)
            node = node.next(c)
        node.eof = True

    def prefix_search(self, word):
        n = len(word)

        node = self.root
        match = None
        buf = ''
        for i in range(n):
            c = word[i]
            node = node.next(c)
            if node is None:
                break
            buf += c
            if node.eof:
                match = buf
        return match


d = ['are', 'area', 'base', 'cat', 'cater', 'children', 'basement']

t = Trie()
for w in d:
    t.insert(w)

print(t.prefix_search('caterer'))
print(t.prefix_search('basemexy'))
print(t.prefix_search('child'))
