class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_left(self, value):
        node = self.Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
            return

        temp = self.head
        self.head = node
        self.head.next = temp
        return

    def add_right(self, value):
        node = self.Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
            return

        self.tail.next = node
        self.tail = self.tail.next
        return

    def append_linked_list(self, ll):
        if self.head is None:
            self.head = ll.head
            self.tail = ll.tail
        else:
            self.tail.next = ll.head
            self.tail = ll.tail

    def reverse_every(self, k):
        cur = self.head

        cnt = 0
        rev = LinkedList()
        buf = LinkedList()

        while cur is not None:
            buf.add_left(cur.value)
            cnt += 1
            cur = cur.next
            if cnt == k or cur is None:
                rev.append_linked_list(buf)
                buf = LinkedList()
                cnt = 0

        return rev

    def to_array(self):
        arr = []

        cur = self.head
        while cur is not None:
            arr.append(cur.value)
            cur = cur.next

        return arr


a = LinkedList()
cur = a.head
for i in range(1, 9):
    a.add_right(i)
print(a.to_array())


r = a.reverse_every(3)
print(r.to_array()) # 3->2->1->6->5->4->8->7

r = a.reverse_every(5)
print(r.to_array()) # 5->4->3->2->1->8->7->6
