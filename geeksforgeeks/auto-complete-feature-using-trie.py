from collections import defaultdict

class Node:
    def __init__(self):
        self.children = defaultdict(lambda: None)
        self.eow = False
        self.count = 0

    def next(self, c):
        return self.children[c]

    def append(self, c):
        self.children[c] = Node()

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        cur = self.root

        n = len(word)
        for i in range(n):
            c = word[i]
            if cur.next(c) is None:
                cur.append(c)
            cur = cur.next(c)
        cur.eow = True
        cur.count += 1

    def recommend(self, prefix, top_k):
        cur = self.root

        n = len(prefix)
        for i in range(n):
            c = prefix[i]
            if cur.next(c) is None:
                return []
            cur = cur.next(c)

        # traverse to find words from the current node
        candidates = find_words(cur, prefix)
        candidates.sort(key=lambda x:x[1])
        candidates.reverse()
        return [w for w, _ in candidates[:3]]


def find_words(root, prefix):
    words = []
    if root.eow == True:
        words.append((prefix, root.count))

    for c, node in root.children.items():
        words += find_words(node, prefix+c)

    return words

# t = Trie()
# history = ['abc', 'abcd','aa', 'abbbaba']
# for w in history:
#     t.insert(w)
# 
# words = t.recommend('ab')
# print(words)

t = Trie()
history = ['hello', 'dog', 'hell', 'cat', 'a', 'hel', 'help', 'helps', 'helping', 'hello', 'help', 'hello']
for w in history:
    t.insert(w)

words = t.recommend('hel', 3)
print(words)
