class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_median(root):
    cnt = count_nodes(root)

    if cnt % 2 == 0:
        target = cnt / 2
        _, m = find_median_even(root, target, 0, None)
        return m
    else:
        target = (cnt + 1) / 2
        _, m = find_median_odd(root, target, 0)
        return m

def count_nodes(root):
    cnt = 0
    if root.left:
        cnt += count_nodes(root.left)
    cnt += 1
    if root.right:
        cnt += count_nodes(root.right)
    return cnt

def find_median_even(root, target, cnt, m):
    if root.left:
        cnt, m = find_median_even(root.left, target, cnt, m)
        if m and cnt > target + 1:
            return cnt, m

    cnt += 1
    if cnt == target:
        m = root.value / 2
    elif cnt == target + 1:
        m += root.value / 2
        return cnt, m

    if root.right:
        cnt, m = find_median_even(root.right, target, cnt, m)
        if m and cnt > target + 1:
            return cnt, m

    return cnt, m

def find_median_odd(root, target, cnt):
    m = None
    if root.left:
        cnt, m = find_median_odd(root.left, target, cnt)
        if m:
            return curr, m
    cnt += 1
    if cnt == target:
        return cnt, root.value
    if root.right:
        cnt, m = find_median_odd(root.right, target, cnt)
        if m:
            return cnt, m
    return cnt, m


root = Node(6)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(4)
root.right = Node(8)
root.right.left = Node(7)
root.right.right = Node(9)
print(find_median(root))

root = Node(6)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(4)
root.right = Node(8)
root.right.left = Node(7)
print(find_median(root))
