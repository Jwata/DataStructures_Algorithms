class Trie:
    def __init__(self):
        self.children = {}
        self.cnt = 0

    def insert(self, word):
        n = len(word)

        node = self
        for i in range(n):
            c = word[i]
            if not c in node.children:
                node.children[c] = Trie()
            node = node.children[c]
            node.cnt += 1

def find_shortest_unique_prefixes(words):
    t = Trie()
    for w in words:
        t.insert(w)

    prefixes = []
    for w in words:
        node = t
        prefix = ""
        for i in range(len(w)):
            if node.cnt == 1:
                break

            prefix += w[i]
            node = node.children[w[i]]
        prefixes.append(prefix)

    return prefixes


words = ["dog", "duck", "dove"]
print(find_shortest_unique_prefixes(words))
