class Queue:
    def __init__(self):
        self.head = None
        self.last = None

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.head = self.last = node
        else:
            last = self.last
            last.next = node
            self.last = node

    def dequeue(self):
        if self.is_empty():
            return None
        head = self.head
        self.head = head.next
        if self.is_empty:
            self.last = None
        return head.value

    def peek(self):
        return self.head.value

    def is_empty(self):
        return self.head == None

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node
