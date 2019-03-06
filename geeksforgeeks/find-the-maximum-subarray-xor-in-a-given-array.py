# O(n^2)
def max_subarray_xor(arr):
    n = len(arr)
    max_xor = None
    for i in range(n):
        cur_xor = 0
        for j in range(i, n):
            cur_xor = cur_xor ^ arr[j]
            if max_xor == None or cur_xor > max_xor:
                max_xor = cur_xor

    return max_xor

# O(n)
class Trie:
    INT_SIZE = 32

    class Node:
        def __init__(self):
            self.value = None
            self.nodes = [None, None]

    def __init__(self):
        root = self.Node()
        self.root = root

    def insert(self, pre_xor):
        cur = self.root

        for i in range(self.INT_SIZE - 1, -1, -1):
            v = bool(pre_xor & (i << i))

            if cur.nodes[v] is None:
                cur.nodes[v] = self.Node()

            cur = cur.nodes[v]

        cur.value = pre_xor

    def query(self, pre_xor):
        cur = self.root

        for i in range(self.INT_SIZE - 1, -1, -1):
            v = bool(pre_xor & (i << i))
            not_v = not v

            if cur.nodes[not_v] is not None:
                cur = cur.nodes[not_v]
            else:
                cur = cur.nodes[v]

        return pre_xor ^ cur.value


def max_subarray_xor_2(arr):
    n = len(arr)

    trie = Trie()
    trie.insert(0)

    pre_xor = 0
    max_xor = None
    for i in range(n):
        pre_xor = pre_xor ^ arr[i]
        trie.insert(pre_xor)

        m = trie.query(pre_xor)
        if max_xor is None or m > max_xor:
            max_xor = m

    return max_xor


arr = [1, 2, 3, 4]
print(max_subarray_xor(arr))  # 7
print(max_subarray_xor_2(arr))  # 7
