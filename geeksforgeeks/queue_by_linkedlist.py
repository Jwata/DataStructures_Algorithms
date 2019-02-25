class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        node = QueueNode(value)
        if self.tail == None and self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        if self.head == None:
            return None
        else:
            tmp = self.head.value
            self.head = self.head.next 
            if self.head == None:
                self.tail = None
            return tmp

    def empty(self):
        return self.head == None


q = Queue()
print(q.dequeue())

q.enqueue(1)
print(q.dequeue())
print(q.dequeue())

q.enqueue(2)
q.enqueue(10)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
