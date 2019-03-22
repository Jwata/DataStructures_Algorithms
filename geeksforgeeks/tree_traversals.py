class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.left.left.left = Node(7)
root.right.right.left = Node(8)

def inorder_dfs(root):
    buf = [root]
    while len(buf) > 0:
        node = buf.pop()
        print(node.value)
        if node.right:
            buf.append(node.right)
        if node.left:
            buf.append(node.left)
print("inorder_dfs")
inorder_dfs(root)

def preorder_dfs(root):
    if root.left:
        preorder_dfs(root.left)
    print(root.value)
    if root.right:
        preorder_dfs(root.right)

print("preorder_dfs")
preorder_dfs(root)


def postorder_dfs(root):
    if root.left:
        postorder_dfs(root.left)
    if root.right:
        postorder_dfs(root.right)
    print(root.value)

print("postorder_dfs")
postorder_dfs(root)
