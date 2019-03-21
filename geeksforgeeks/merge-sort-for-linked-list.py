class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None

    def push(self, value):
        node = self.Node(value)

        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def pop(self):
        if not self.head:
            return None

        head = self.head
        self.head = head.next
        return head

    def divide_half(self):
        if self.head is None:
            return LinkedList(), LinkedList()

        fast = self.head.next
        slow = self.head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        half2 = LinkedList()
        half2.head = slow.next
        slow.next = None
        half1 = self

        return half1, half2

    def to_array(self):
        arr = []
        cur = self.head
        while cur:
            arr.append(cur.value)
            cur = cur.next

        return arr

def merge_sort(a):
    if not a.head or not a.head.next:
        return a

    h1, h2 = a.divide_half()
    sorted1 = merge_sort(h1)
    sorted2 = merge_sort(h2)

    return merge_sorted(sorted1, sorted2)

def merge_sorted(a, b):
    head = None
    prev = None

    while a.head or b.head:
        if a.head and b.head:
            if a.head.value < b.head.value:
                cur = a.pop()
            else:
                cur = b.pop()
        elif a.head:
            cur = a.pop()
        else:
            cur = b.pop()

        if head is None:
            head = cur
        if prev:
            prev.next = cur
        prev = cur

    s = LinkedList()
    s.head = head
    return s


# construct linked list
a = LinkedList()
a.push(30)
a.push(50)
a.push(10)
a.push(60)
a.push(20)
a.push(40)
print(a.to_array())

s = merge_sort(a)
print(s.to_array())

# a, b = a.divide_half()
# print(a.to_array())
# print(b.to_array())

# c = LinkedList()
# c.push(30)
# c.push(20)
# c.push(10)
# d = LinkedList()
# d.push(40)
# d.push(15)
# d.push(5)
# s = merge_sorted(c, d)
# print(s.to_array())
