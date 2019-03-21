class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
    
    def __init__(self):
        self.head = None

    def push(self, value):
        node = self.Node(value)

        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def detect_loop(self):
        cur = self.head
        visited = set()

        while cur:
            visited.add(id(cur))
            if cur.next and id(cur.next) in visited:
                cur.next = None
                return True
            cur = cur.next

        return False

    def to_array(self):
        arr = []

        cur = self.head
        while cur:
            arr.append(cur.value)
            cur = cur.next

        return arr


a = LinkedList()
a.push(5)
a.push(4)
a.push(3)
a.push(2)
a.push(1)

print(a.detect_loop()) # False
print(a.to_array()) # [1,2,3,4,5]

# make loop
tail = a.head.next.next.next.next
tail.next = a.head.next

print(a.detect_loop()) # True
print(a.to_array()) # [1,2,3,4,5]
