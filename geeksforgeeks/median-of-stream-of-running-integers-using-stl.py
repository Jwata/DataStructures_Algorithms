import heapq

class Consumer:
    def __init__(self):
        self.high = [] # min heap
        self.low = [] # max heap

    def add(self, value):
        n_high = len(self.high)
        n_low = len(self.low)

        to_high = None

        if n_high == 0 and n_low == 0:
            to_high = True
        elif n_high < n_low:
            if value <= self.low[0]:
                tmp = self.pop_low()
                self.add_high(tmp)
            else:
                to_high = True
        elif n_low < n_high:
            if value >= self.high[0]:
                tmp = self.pop_high()
                self.add_low(tmp)
                to_high = True
            else:
                if value > self.low[0]:
                    to_high = True

        if to_high:
            self.add_high(value)
        else:
            self.add_low(value)

    def add_high(self, value):
        heapq.heappush(self.high, value)

    def pop_high(self):
        return heapq.heappop(self.high)

    def min_high(self):
        return self.high[0]

    def add_low(self, value):
        heapq.heappush(self.low, -1 * value)

    def pop_low(self):
        tmp = heapq.heappop(self.high)
        return -1 * tmp

    def max_low(self):
        return -1 * self.low[0]

    def median(self):
        n_high = len(self.high)
        n_low = len(self.low)

        if n_high == 0 and n_low == 0:
            return None
        elif n_high == n_low:
            return (self.min_high() + self.max_low()) / 2
        elif n_high > n_low:
            return self.min_high()
        else:
            return self.max_low()

c = Consumer()
xs = [5, 15, 10, 20, 3]
for x in xs:
    c.add(x)
    print(c.median())
