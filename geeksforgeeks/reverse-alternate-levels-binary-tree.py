class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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

def postorder_print(root):
    if root is None:
        return

    postorder_print(root.left)
    postorder_print(root.right)
    print(root.value)

def bfs_print(root):
    q = [root]

    while len(q) > 0:
        c = q.pop(0)
        print(c.value)
        if c.left:
            q.append(c.left)
        if c.right:
            q.append(c.right)

# Two traversal
def reverse_alternate(root):
    stack = []
    store_alternate(root, stack, 0)
    replace_alternate(root, stack, 0)

def store_alternate(root, stack, depth):
    if root is None:
        return

    store_alternate(root.left, stack, depth+1)

    if depth % 2 == 1:
        stack.append(root.value)

    store_alternate(root.right, stack, depth+1)

def replace_alternate(root, stack, depth):
    if root is None:
        return
    replace_alternate(root.left, stack, depth+1)

    if depth % 2 == 1:
        root.value = stack.pop()

    replace_alternate(root.right, stack, depth+1)

# (Optimal) One traversal
# def reverse_alternate_optimal(root):
#     preorder_swap(root.left, root.right, 1)
# 
# def preorder_swap(node1, node2, depth):
#     if node1 is None or node1 is None:
#         return
#     if depth % 2 == 1:
#         # swap values
#         node1.value, node2.value = node2.value, node1.value
# 
#     preorder_swap(node1.left, node2.right, depth+1)
#     preorder_swap(node1.right, node2.left, depth+1)

root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.left.left = Node('d')
root.left.right = Node('e')
root.right.left = Node('f')
root.right.right = Node('g')
root.left.left.left = Node('h')
root.left.left.right = Node('i')
root.left.right.left = Node('j')
root.left.right.right = Node('k')
root.right.left.left = Node('l')
root.right.left.right = Node('m')
root.right.right.left = Node('n')
root.right.right.right = Node('o')

reverse_alternate(root)

print("BFS")
bfs_print(root)

# print("DFS inorder")
# inorder_print(root)
# 
# print("DFS preorder")
# preorder_print(root)
# 
# print("DFS postorder")
# postorder_print(root)
