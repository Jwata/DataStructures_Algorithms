class Heap:
    def __init__(self):
        self.arr = []

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def size(self):
        return len(self.arr)

    def empty(self):
        return self.size() == 0

    def head(self):
        return self.arr[0] # raise error if heap is empty

    def push(self, v):
        self.arr.append(v)

        i = len(self.arr) - 1
        while i > 0:
            j = (i-1)//2
            if self.arr[j] < self.arr[i]:
                break

            self.swap(i, j)
            i = j

    def pop(self):
        if self.size() == 1:
            return self.arr.pop()

        root = self.arr[0] # raise error if heap is empty
        self.arr[0] = self.arr.pop()

        i = 0
        while i < self.size():
            left = i * 2 + 1
            right = left + 1

            if left < self.size() and self.arr[left] < self.arr[i]:
                self.swap(i, left)
                i = left
            elif right < self.size() and self.arr[right] < self.arr[i]:
                self.swap(i, right)
                i = right
            else:
                break

        return root


h = Heap()
h.push(4)
h.push(8)
h.push(11)
h.push(7)
h.push(3)
h.push(9)

print(h.arr)
while not h.empty():
    print(h.pop(), h.arr)
