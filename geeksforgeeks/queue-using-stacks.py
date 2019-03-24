class Stack:
    def __init__(self):
        self.buf = []

    def push(self, value):
        self.buf.append(value)

    def pop(self):
        return self.buf.pop()

    def empty(self):
        return len(self.buf) == 0

class QueueEnqueCostly:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enque(self, value):
        while not self.s1.empty():
            self.s2.push(self.s1.pop())

        self.s2.push(value)

        while not self.s2.empty():
            self.s1.push(self.s2.pop())

    def deque(self):
        if self.s1.empty():
            return None
        return self.s1.pop()

class QueueDequeCostly:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enque(self, value):
        self.s1.push(value)

    def deque(self):
        if self.s1.empty():
            return None

        while not self.s1.empty():
            self.s2.push(self.s1.pop())
        tmp = self.s2.pop()

        while not self.s2.empty():
            self.s1.push(self.s2.pop())

        return tmp

q = QueueEnqueCostly()
q.enque(1)
q.enque(2)
q.enque(3)
print(q.deque())
q.enque(4)
print(q.deque())
print(q.deque())
print(q.deque())
print(q.deque())
