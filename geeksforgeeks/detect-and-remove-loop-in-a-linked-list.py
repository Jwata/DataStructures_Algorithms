class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.visited = False
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

        while cur:
            cur.visited = True
            if cur.next and cur.next.visited:
                cur.next = None
                return True
            cur = cur.next

        return False

    def reset_visited(self):
        cur = self.head
        while cur:
            cur.visited = False
            cur = cur.next

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
a.reset_visited()

# make loop
tail = a.head.next.next.next.next
tail.next = a.head.next

print(a.detect_loop()) # True
print(a.to_array()) # [1,2,3,4,5]
