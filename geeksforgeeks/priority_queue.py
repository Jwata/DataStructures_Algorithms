class PriorityQueue:
    def __init__(self):
        self.arr = []
        self.pos = {}

    def swap(self, i, j):
        pi, qi = self.arr[i]
        pj, qj = self.arr[j]

        self.arr[i] = (pj, qj)
        self.arr[j] = (pi, qi)

        self.pos[qi] = j
        self.pos[qj] = i

    def size(self):
        return len(self.arr)

    def empty(self):
        return self.size() == 0

    def head(self):
        return self.arr[0] # raise error if heap is empty

    def push(self, p, q):
        self.arr.append((p, q))

        i = self.size() - 1
        self.pos[q] = i

        while i > 0:
            j = (i-1)//2
            if self.arr[j][0] < self.arr[i][0]:
                break

            self.swap(i, j)
            i = j

    def pop(self):
        if self.size() == 1:
            self.pos.pop(self.arr[0][1])
            return self.arr.pop()

        root = self.arr[0] # raise error if heap is empty
        self.pos.pop(root[1])
        self.arr[0] = self.arr.pop()
        self.pos[self.arr[0][1]] = 0

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

    def has(self, q):
        return q in self.pos

    def priority(self, q):
        if q in self.pos:
            self.pos[q]


if __name__ == '__main__':
    h = PriorityQueue()
    h.push(4, "tokyo")
    h.push(8, "nagoya")
    h.push(11, "osaka")
    h.push(7, "sapporo")
    h.push(3, "fukuoka")
    h.push(9, "naha")
    print("Pushed result")
    print(h.arr)
    print(h.pos)

    import ipdb; ipdb.set_trace()

    while not h.empty():
        print("Pop")
        print(h.pop())
        print(h.arr)
        print(h.pos)
