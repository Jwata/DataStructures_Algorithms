class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        self.head = Node(value, next_node=self.head)

    def pop(self):
        if self.is_empty():
            return None
        poped = self.head
        self.head = poped.next
        return poped.value

    def peak(self):
        if self.is_empty():
            return None
        return self.head.value

    def is_empty(self):
        return self.head == None

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node
