class Queue:
    def __init__(self):
        self.q = []
    
    def enque(self, value):
        self.q.append(value)

    def deque(self):
        return self.q.pop(0)

    def rear(self):
        return self.q[-1]

    def front(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0

class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, value):
        self.q1.enque(value)

    def pop(self):
        while self.q1.rear() != self.q1.front():
            self.q2.enque(self.q1.deque())
        tmp = self.q1.deque()
        self.q1, self.q2 = self.q2, self.q1
        return tmp

class StackPushCostly:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, value):
        self.q2.enque(value)

        while not self.q1.empty():
            self.q2.enque(self.q1.deque())

        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.deque()


stack = StackPushCostly()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())
print(stack.pop())
stack.push(4)
print(stack.pop())
print(stack.pop())
