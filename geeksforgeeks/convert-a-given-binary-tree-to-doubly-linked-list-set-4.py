class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class DLL:
    class Node:
        def __init__(self, value):
                self.value = value
                self.next = None
                self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        node = self.Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
            return

        self.tail.next = node
        node.prev = self.tail

        self.tail = node

    def append_dll(self, dll):
        if dll.head is None:
            return

        self.tail.next = dll.head
        dll.head.prev = self.tail

        self.tail = dll.tail

    def print_traverse(self):
        cur = self.head
        while cur:
            print(cur.value)
            cur = cur.next

def convert_to_dll(tree_node):
    if tree_node is None:
        return DLL()

    dll = convert_to_dll(tree_node.left)

    dll.append(tree_node.value)

    next_dll = convert_to_dll(tree_node.right)
    dll.append_dll(next_dll)

    return dll


root = TreeNode(10)
root.left = TreeNode(12)
root.right = TreeNode(15)
root.left.left = TreeNode(25)
root.left.right = TreeNode(30)
root.right.left = TreeNode(36)

dll = convert_to_dll(root)
# dll.print_traverse()


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
def convert_to_dll(root):
    left = None
    right = None

    if root.left:
        left, right = convert_to_dll(root.left) 
        right.right = root
        root.left = right
        right = root
    else:
        left = root
        right = root
    
    if root.right:
        next_left, next_right = convert_to_dll(root.right)
        right.right = next_left
        next_left.left = right
        right = next_right
    
    return left, right

def traverse_print_dll(head):
    while head:
        print(head.value)
        head = head.right 

root = Node(10)
root.left = Node(12)
root.right = Node(15)
root.left.left = Node(25)
root.left.right = Node(30)
root.right.left = Node(36)

head, tail = convert_to_dll(root)
traverse_print_dll(head)
