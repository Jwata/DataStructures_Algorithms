class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# O(n^2) this is not optimal solution
def mps_bsf(node):
    max_mps = None

    q = [node]
    while len(q) > 0:
        cur = q.pop(0)
        s = mps(node)
        if max_mps is None or s > max_mps:
            max_mps = s
        q.append(cur.left)
        q.append(cur.right)

    return max_mps

def mps(node):
    s = node.value
    if node.left is not None:
        left_s  = _mps(node.left)
        if left_s > 0:
            s += left_s
    if node.right is not None:
        right_s = _mps(node.right)
        if right_s > 0:
            s += right_s
    return s

def _mps(node):
    if node is None:
        return 0

    s = node.value
    left_s = _mps(node.left)
    right_s = _mps(node.right)

    if left_s is not None and right_s is not None:
        return s + max([left_s, right_s, 0])
    elif left_s is not None:
        return s + max([left_s, 0])
    elif right_s is not None:
        return s + max([right_s, 0])

# for testing
root = Node(10)
root.left = Node(2)
root.left.left = Node(20)
root.left.right = Node(1)
root.right = Node(10)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)

def print_bfs(root):
    q = [root]
    while len(q) > 0:
        cur = q.pop(0)
        print(cur.value)
        q.append(cur.left)
        q.append(cur.right)


print(mps(root))
