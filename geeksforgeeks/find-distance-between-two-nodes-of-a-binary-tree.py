class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def distance(root, t1, t2):
    d1, d2, dp = postorder_search(root, t1, t2, 0)
    return (d1 - dp) + (d2 - dp)

# O(n)
def postorder_search(root, t1, t2, d):
    if root is None:
        return None, None, None
    d1, d2, dp = None, None, None

    d1_l, d2_l, dp_l = postorder_search(root.left, t1, t2, d+1)
    if d1_l and d2_l and dp_l:
        return d1_l, d2_l, dp_l
    if d1_l:
        d1 = d1_l
    if d2_l:
        d2 = d2_l
    if dp_l:
        dp = dp_l

    d1_r, d2_r, dp_r = postorder_search(root.right, t1, t2, d+1)
    if d1_r and d2_r and dp_r:
        return d1_r, d2_r, dp_r
    if d1_r:
        d1 = d1_r
    if d2_r:
        d2 = d2_r
    if dp_r:
        dp = dp_r

    if root.value == t1:
        d1 = d
    elif root.value == t2:
        d2 = d

    if d1 and d2 and dp is None:
        dp = d

    return d1, d2, dp


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)

print(distance(root, 4, 5))
print(distance(root, 4, 6))
print(distance(root, 3, 4))
print(distance(root, 2, 4))
print(distance(root, 8, 5))
