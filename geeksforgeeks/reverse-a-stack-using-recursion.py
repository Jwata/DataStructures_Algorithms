class Stack:
    def __init__(self):
        self.buf = []

    def is_empty(self):
        return len(self.buf) == 0

    def push(self, value):
        self.buf.append(value)

    def pop(self):
        return self.buf.pop()

    def reverse(self):
        rev = Stack()
        return reverse_stack_helper(self, rev)

    def to_array(self):
        return self.buf

def reverse_stack_helper(stack, rev):
    if stack.is_empty():
        return rev

    rev.push(stack.pop())
    return reverse_stack_helper(stack, rev)


s = Stack()
s.push(1)
s.push(3)
s.push(4)

rev = s.reverse()
print(rev.pop()) # 1
print(rev.pop()) # 3
print(rev.pop()) # 4
print(rev.pop()) # error
