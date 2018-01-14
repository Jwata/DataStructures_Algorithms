class BinaryTreeNode:

  def __init__(self, value):
      self.value = value
      self.left  = None
      self.right = None

  def insert_left(self, value):
      self.left = BinaryTreeNode(value)
      return self.left

  def insert_right(self, value):
      self.right = BinaryTreeNode(value)
      return self.right

def is_superbalanced(root):

    nodes = []
    if root.left:
        nodes.append(root.left)
    if root.right:
        nodes.append(root.right)

    depth = 1
    min_depth = None

    children = []
    current = None

    while len(nodes) > 0:
        current = nodes.pop()

        if current.left:
            children.append(current.left)
        if current.right:
            children.append(current.right)

        if not current.left and not current.right:
            if not min_depth:
                min_depth = depth

        if len(nodes) == 0:
            depth += 1
            nodes = children
            children = []

    return depth - min_depth <= 1

# depth 0
root = BinaryTreeNode(1)

# depth 1
root.insert_left(2)
root.insert_right(3)

# depth 2
root.left.insert_left(4)
root.right.insert_left(5)

# depth 3
root.left.left.insert_left(6)

print(is_superbalanced(root)) # should be False

# depth 0
root = BinaryTreeNode(1)

# depth 1
root.insert_left(2)
root.insert_right(3)

# depth 2
root.left.insert_left(4)
root.right.insert_left(5)

print(is_superbalanced(root)) # should be True
