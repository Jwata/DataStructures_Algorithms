class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def construct_tree(pre, post):
    post_map = {}
    for i, v in enumerate(post):
        post_map[v] = i

    n = len(post)
    return construct_tree_helper(pre, post, post_map, 0, n-1)

def construct_tree_helper(pre, post, post_map, post_from, post_to):
    if len(pre) == 0:
        return
    if post_from > post_to:
        return

    v = pre.pop(0)
    root = Node(v)
    
    if len(pre) == 0:
        return root
    
    left_v = pre[0]
    left_pos = post_map[left_v]
    
    if left_pos > post_to:
        return root

    root.left = construct_tree_helper(
        pre, post, post_map, post_from, left_pos)
    root.right = construct_tree_helper(
        pre, post, post_map, left_pos+1, post_to-1)
    
    return root

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

# pre = [1, 2, 3, 4, 5 ,6, 7]
# post = [2, 4, 6, 7, 5, 3, 1]
pre = [1, 2, 4, 8, 9, 5, 3, 6, 7]
post = [8, 9, 4, 5, 2, 6, 7, 3, 1]

root = construct_tree(pre, post)
print("preoder print")
preorder_print(root)
print("postoder print")
postorder_print(root)
