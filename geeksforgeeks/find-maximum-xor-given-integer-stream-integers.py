class Node:
    def __init__(self):
        self.children = [None, None]

    def next(self, b):
        return self.children[b]

    def append(self, b):
        self.children[b] = Node()

class Trie:
    NUM_BITS = 30

    def __init__(self):
        self.root = Node()

    def insert(self, x):
        cur = self.root
        for bit_pos in range(self.NUM_BITS-1, -1, -1):
            if x & (1 << bit_pos):
                b = 1
            else:
                b = 0

            if cur.next(b) is None:
                cur.append(b)
            cur = cur.next(b)

    def max_xor(self, y):
        cur = self.root
        xor = 0
        for bit_pos in range(self.NUM_BITS-1, -1, -1):
            if y & (1 << bit_pos):
                b_op = 0
                b = 1
            else:
                b_op = 1
                b = 0

            if cur.next(b_op):
                cur = cur.next(b_op)
                xor |= (1 << bit_pos)
            else:
                cur = cur.next(b)

        return xor

inputs = [(1, 10), (1, 13), (2, 10), (1, 9), (1, 5), (2, 6)]

t = Trie()
for q_type, value in inputs:
        if q_type == 1:
            t.insert(value)
        elif q_type == 2:
            xor = t.max_xor(value)
            print(xor)
