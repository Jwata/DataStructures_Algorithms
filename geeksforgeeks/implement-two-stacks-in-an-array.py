class TwoStacks:
    def __init__(self):
        self.buf = []
        self.size1 = 0
        self.size2 = 0

    def push1(self, value):
        self.buf = [value] + self.buf
        self.size1 += 1

    def pop1(self):
        if self.size1 == 0:
            return None
        self.size1 -= 1
        return self.buf.pop(0)

    def push2(self, value):
        self.buf.append(value)
        self.size2 += 1

    def pop2(self):
        if self.size2 == 0:
            return None
        self.size2 -= 1
        return self.buf.pop()

ts = TwoStacks()
ts.push1(1)
ts.push1(2)
ts.push2(3)
ts.push2(4)
print(ts.pop1()) # 1
print(ts.pop2()) # 4
print(ts.pop1()) # 2
print(ts.pop1()) # None
print(ts.pop2()) # 3
print(ts.pop2()) # None
