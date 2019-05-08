from collections import defaultdict
import heapq

class Node:
    def __init__(self, value=None, freq=0):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None

    def add_node(self, node):
        if self.left is None:
            self.left = node
        elif self.right is None:
            self.right = node
        else:
            raise Exception('this node is already full')

        self.freq += node.freq

    def is_full(self):
        return self.left and self.right

    def __lt__(self, _):
        return True


def huffman_code(xs):
    freqs = count_freqs(xs)
    h = build_min_heap(freqs)
    root = construct_huffman_tree(h)
    codes = get_codes(root)
    return codes
    # print(codes)
    # return assign_codes(xs, codes)

def count_freqs(xs):
    freqs = defaultdict(lambda: 0)
    for x in xs:
        for i in range(len(x)):
            c = x[i]
            freqs[c] += 1
    return freqs

def build_min_heap(freqs):
    h = []
    for c, f in freqs.items():
        node = Node(c, f)
        heapq.heappush(h, (f, node))
    return h

def construct_huffman_tree(h):
    root = Node()

    while len(h) > 0:
        if root.is_full():
            heapq.heappush(h, (root.freq, root))
            root = Node()

        freq, node = heapq.heappop(h)
        root.add_node(node)

    return root

def get_codes(root):
    codes = {}
    traverse(root, '', codes)
    return codes

def traverse(root, pre, codes):
    if root.value:
        codes[root.value] = pre
        return
    if root.left:
        traverse(root.left, pre + '0', codes)
    if root.right:
        traverse(root.right, pre + '1', codes)

def assign_codes(xs, codes):
    n = len(xs)
    xs_coded = []
    for i in range(n):
        x = xs[i]
        m = len(x)
        coded = ''
        for j in range(m):
            coded += codes[x[j]]
        xs_coded.append(coded)

    return xs_coded

xs = ['cccd', 'cb', 'acd', 'ab']
print(huffman_code(xs))
