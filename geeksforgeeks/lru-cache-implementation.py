class LRUCache:
    class Node:
        def __init__(self, key):
            self.key = key
            self.next = None
            self.prev = None

    def __init__(self, m):
        self.m = m # cache size
        self.head = None
        self.tail = None
        self.cache = {}

    # O(1)
    def refer(self, k):
        if k in self.cache:
            self.delete(k)
        else:
            if len(self.cache) >= self.m:
                self.delete(self.head.key)

        self.push(k)
        return self.tail.key

    def push(self, k):
        node = self.Node(k)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.cache[node.key] = node

    def delete(self, k):
        node = self.cache[k]
        if node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
        elif node.prev is None:
            self.head = node.next
            node.next.prev = None
        else:
            self.tail = node.prev
            node.prev.next = None
        self.cache.pop(k)


def print_cache(c):
    tmp = []
    cur = c.head
    while cur:
        tmp.append(cur.key)
        cur = cur.next
    print(tmp)

cache = LRUCache(3)
cache.refer(1)
print_cache(cache)
cache.refer(2)
print_cache(cache)
cache.refer(3)
print_cache(cache)
cache.refer(1)
print_cache(cache)
cache.refer(4)
print_cache(cache)
