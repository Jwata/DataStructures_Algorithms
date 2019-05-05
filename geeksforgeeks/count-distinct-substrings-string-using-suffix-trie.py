from collections import defaultdict

class Node:
    def __init__(self):
        self.children = defaultdict(lambda: None)

    def next(self, c):
        if self.children[c] is None:
            self.children[c] = Node()
        return self.children[c]

class Trie:
    def __init__(self, s):
        self.root = Node()

        n = len(s)
        for i in range(n):
            sub_s = s[i:]
            self.insert(sub_s)

    def insert(self, s):
        cur = self.root 
        n = len(s)
        for i in range(n):
            cur = cur.next(s[i])

    def count_substr(self):
        return count_nodes(self.root) # include empty substring

def count_nodes(root):
    cnt = 1
    for _, node in root.children.items():
        cnt += count_nodes(node)
    return cnt

t = Trie('ababa')
print(t.count_substr())

t = Trie('abcba')
print(t.count_substr())
