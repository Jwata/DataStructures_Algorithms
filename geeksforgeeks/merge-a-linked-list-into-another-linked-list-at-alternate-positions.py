class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head  = None

    def empty(self):
        return self.head is None

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return

        cur = self.head
        while cur.next is not None:
            cur = cur.next

        cur.next = node

    def pop(self):  # error if empty
        head = self.head
        self.head = self.head.next
        head.next = None
        return head

    def to_array(self):
        arr = []

        cur = self.head
        while cur is not None:
            arr.append(cur.value)
            cur = cur.next

        return arr


a = LinkedList()
a.append(5)
a.append(7)
a.append(17)
a.append(13)
a.append(11)

b = LinkedList()
b.append(12)
b.append(10)
b.append(2)
b.append(4)
b.append(6)


def merge(a, b):
    cur = a.head

    while cur is not None and not b.empty():
        temp = cur.next
        cur.next = b.pop()
        cur.next.next = temp
        cur = temp

    return a, b

a.pop()
a.pop()
a, b = merge(a, b)
print(a.to_array())
print(b.to_array())
