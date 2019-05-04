from copy import copy

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Constructing map O(n)
# Traverse O(n)
def construct_tree_wapper(inorder_seq, preorder_seq):
    inorder_map = {}
    for i, v in enumerate(inorder_seq):
        inorder_map[v] = i

    n = len(inorder_seq)

    return construct_tree(inorder_seq, preorder_seq, inorder_map, 0, n-1)

def construct_tree(
        inorder_seq, preorder_seq, inorder_map, inorder_from, inorder_to):

    if inorder_from > inorder_to:
        return None

    v = preorder_seq.pop(0)
    root = Node(v)

    root_pos = inorder_map[v]

    root.left = construct_tree(
        inorder_seq, preorder_seq, inorder_map, inorder_from, root_pos - 1)
    root.right = construct_tree(
        inorder_seq, preorder_seq, inorder_map, root_pos + 1, inorder_to)

    return root

def inorder_print(root):
    if root is None:
        return
    inorder_print(root.left)
    print(root.value)
    inorder_print(root.right)

def preorder_print(root):
    if root is None:
        return
    print(root.value)
    preorder_print(root.left)
    preorder_print(root.right)

inorder_seq = ['D', 'B', 'E', 'A', 'F', 'C']
preorder_seq = ['A', 'B', 'D', 'E', 'C', 'F']

root = construct_tree_wapper(inorder_seq, copy(preorder_seq))
print("inorder")
print("expected", inorder_seq)
inorder_print(root)
print("preorder")
print("expected", preorder_seq)
preorder_print(root)
