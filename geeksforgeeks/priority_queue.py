class PriorityQueue:
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

    def push(self, p, q):
        self.arr.append((p, q))

        i = self.size() - 1
        while i > 0:
            j = (i-1)//2
            if self.arr[j][0] < self.arr[i][0]:
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
            l = i * 2 + 1
            r = l + 1

            if l < self.size() and self.arr[l][0] < self.arr[i][0]:
                self.swap(i, l)
                i = l
            elif r < self.size() and self.arr[r][0] < self.arr[i][0]:
                self.swap(i, r)
                i = r
            else:
                break

        return root


if __name__ == '__main__':
    h = PriorityQueue()
    h.push(4, "tokyo")
    h.push(8, "nagoya")
    h.push(11, "osaka")
    h.push(7, "sapporo")
    h.push(3, "fukuoka")
    h.push(9, "naha")
    print(h.arr)

    while not h.empty():
        print(h.pop(), h.arr)
