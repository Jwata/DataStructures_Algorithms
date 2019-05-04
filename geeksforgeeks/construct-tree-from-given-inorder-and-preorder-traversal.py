class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def construct_tree(inorder_seq, preorder_seq):
    if len(inorder_seq) == 0:
        return None

    v = preorder_seq.pop(0)
    root = Node(v)

    is_left = True
    left_inorder_seq = []
    right_inorder_seq = []
    for v_in in inorder_seq:
        if v == v_in:
            is_left = False
        else:
            if is_left:
                left_inorder_seq.append(v_in)
            else:
                right_inorder_seq.append(v_in)

    root.left = construct_tree(left_inorder_seq, preorder_seq)
    root.right = construct_tree(right_inorder_seq, preorder_seq)
    return root

# def bfs_print(root):
#     q = [root]
#     while len(q) > 0:
#         cur = q.pop(0)
#         print(cur.value)
#         if cur.left:
#             q.append(cur.left)
#         if cur.right:
#             q.append(cur.right)

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

from copy import copy
root = construct_tree(inorder_seq, copy(preorder_seq))
print("inorder")
print("expected", inorder_seq)
inorder_print(root)
print("preorder")
print("expected", preorder_seq)
preorder_print(root)
