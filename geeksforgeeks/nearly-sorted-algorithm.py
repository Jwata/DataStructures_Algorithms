class Heap:
    def __init__(self):
        self.buf = []

    def push(self, value):
        self.buf.append(value)
        i = self.size() - 1
        while i > 0:
            pi = (i - 1) // 2
            if self.buf[pi]  <= self.buf[i]:
                break
            self.swap(i, pi)
            i = pi

    def pop(self):
        if self.size() == 1:
            return self.buf.pop()

        head = self.buf[0]
        self.buf[0] = self.buf.pop()

        i = 0
        n = self.size()
        while i < n:
            l = i * 2 + 1
            r = l + 1
            smallest = i

            if l < n and self.buf[i] > self.buf[l]:
                smallest = l
            if  r < n and self.buf[smallest] > self.buf[r]:
                smallest = r

            if smallest == i:
                break

            self.swap(i, smallest)
            i = smallest

        return head

    def size(self):
        return len(self.buf)

    def swap(self, i, j):
        self.buf[i], self.buf[j] = self.buf[j], self.buf[i]

# n = 7
# k = 3
# i = 4
# heap = [5, 6, 8, 10]
# arr= [2, 3, 3, 2, 8, 10, 9]
def sort_k_sorted_array(arr, k):
    n = len(arr)

    heap = Heap()

    for i in range(n+k+1):
        if i > k:
            arr[i-k-1] = heap.pop()
            if i < n:
                heap.push(arr[i])
        else:
            heap.push(arr[i])

    return arr


arr= [6, 5, 3, 2, 8, 10, 9]
k = 3

print(sort_k_sorted_array(arr, k))
