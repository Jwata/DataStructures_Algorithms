class Tree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def is_leaf(self):
            return self.left is None and self.right is None

        def has_both_children(self):
            return (self.left is not None) and (self.right is not None)

    def __init__(self):
        self.root = None

    def check_fbt(self):
        if self.root is None:
            return True

        buf = [self.root]

        while len(buf) > 0:
            cur = buf.pop()
            print(cur.value)

            if cur.right is not None:
                buf.append(cur.right)
            if cur.left is not None:
                buf.append(cur.left)

            if cur.is_leaf() == False and cur.has_both_children() == False:
                return False

        return True

t = Tree()
t.root = Tree.Node(1)
t.root.left = Tree.Node(2)
t.root.right = Tree.Node(3)
t.root.left.left = Tree.Node(4)
t.root.left.right = Tree.Node(5)

# time O(n)
print(t.check_fbt())

# Recursive version
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.left is None and self.right is None

    def has_both_children(self):
        return (self.left is not None) and (self.right is not None)

    def is_full(self):
        print(self.value)
        if self.is_leaf():
            return True
        if self.has_both_children():
            return self.left.is_full() and self.right.is_full()
        return False

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(root.is_full())
