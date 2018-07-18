class MaxHeap:
    def __init__(self, value=None):
        self.buffer = []

    def empty(self):
        return len(self.buffer) == 0

    def peek(self):
        if self.empty():
            return None
        else:
            return self.buffer[0]

    def push(self, value):
        self.buffer.append(value)
        self._upheap(len(self.buffer)-1)

    def _upheap(self, idx):
        p_idx = (idx - 1) // 2
        # print('Parent at {}: {}, Child at {}: {}'.format(p_idx, self.buffer[p_idx], idx, self.buffer[idx]))

        if p_idx < 0:
            return
        elif self.buffer[p_idx] < self.buffer[idx]:
            self.buffer[p_idx], self.buffer[idx] = \
                    self.buffer[idx], self.buffer[p_idx]
            return self._upheap(p_idx)

    def pop(self):
        last = self.buffer.pop()
        if self.empty():
            return last
        max_value = self.buffer[0]

        # Rearrange the remainings
        self.buffer[0] = last
        self._downheap(0)

        return max_value

    def _downheap(self, idx):
        cl_idx = 2 * idx + 1
        cr_idx = cl_idx + 1

        if len(self.buffer) - 1 < cl_idx:
            return

        if len(self.buffer) - 1 >= cr_idx and self.buffer[cr_idx] > self.buffer[cl_idx]:
            c_idx = cr_idx
        else:
            c_idx = cl_idx

        # print('Parent at {}: {}, Child at {}: {}'.format(idx, self.buffer[idx], cl_idx, self.buffer[cl_idx]))

        if self.buffer[idx] < self.buffer[c_idx]:
             self.buffer[idx], self.buffer[c_idx] = \
                     self.buffer[c_idx], self.buffer[idx]
             self._downheap(c_idx)

heap = MaxHeap()

heap.push(1)
heap.push(2)
heap.push(5)
heap.push(3)
heap.push(4)
heap.push(2)

assert heap.peek() == 5
assert heap.buffer == [5, 4, 2, 1, 3, 2]

assert heap.pop() == 5
assert heap.buffer == [4, 3, 2, 1, 2]

assert heap.pop() == 4
assert heap.buffer == [3, 2, 2, 1]

assert heap.pop() == 3
assert heap.buffer == [2, 1, 2]

assert heap.pop() == 2
assert heap.buffer == [2, 1]

assert heap.pop() == 2
assert heap.buffer == [1]

assert heap.pop() == 1
assert heap.empty()

print('Passed all assertions')
