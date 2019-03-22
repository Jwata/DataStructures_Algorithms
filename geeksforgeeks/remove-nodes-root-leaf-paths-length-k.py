class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.left is None and self.right is None

class Tree:
    def __init__(self):
        self.root = None

    def remove_nodes_less_than(self, k, l):
        delte_root = remove_nodes_less_than_helper(self.root, k, l)
        if delte_root:
            self.root = None

    def print_bfs(self):
        if not self.root:
            return

        q = [self.root]
    
        while len(q) > 0:
            node = q.pop(0)
            print(node.value)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

def remove_nodes_less_than_helper(root, k, l):
    if root.is_leaf():
        return k > l

    delete_left = None
    if root.left:
        delete_left = remove_nodes_less_than_helper(root.left, k, l+1)
        if delete_left:
            root.left = None

    delete_right = None
    if root.right:
        delete_right = remove_nodes_less_than_helper(root.right, k, l+1)
        if delete_right:
            root.right = None

    if delete_left is None:
        return delete_right
    elif delete_right is None:
        return delete_left
    return delete_left and delete_right


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.right = Node(6)
root.right.right.left = Node(8)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(7)

tree = Tree()
tree.root = root
tree.remove_nodes_less_than(4, 1)
tree.print_bfs()
