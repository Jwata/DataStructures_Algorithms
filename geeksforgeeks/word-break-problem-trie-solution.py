class Trie:
    def __init__(self):
        self.nexts = {}
        self.eow = False

    def is_leaf(self):
        return len(self.nexts) == 0

    def insert(self, word):
        n = len(word)
        cur = self
        for i in range(n):
            c = word[i]
            if not c in cur.nexts:
                cur.nexts[c] = Trie()
            cur = cur.nexts[c]

        cur.eow = True

def word_break(string, d):
    t = Trie()
    for w in d: # O(kn)
        t.insert(w)

    return word_break_helper(string, t, 0, [])

def word_break_helper(string, t, i, sentence):
    n = len(string)
    if i >= n:
        return [sentence]

    sentences = []
    word = ""
    cur = t
    while i < n and cur: # O(k^2)
        c = string[i]
        if not c in cur.nexts:
            return sentences

        word += c # like
        cur = cur.nexts[c]

        if cur.eow:
            sentences += word_break_helper(string, t, i+1, sentence + [word])
        i += 1

    return sentences


d = ["i", "like", "sam", "sung", "samsung"]
s = "ilikesamsung"
print(word_break(s, d))

# TimeComplexity: O(kn + k^2)
