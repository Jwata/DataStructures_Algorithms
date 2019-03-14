def compare(l1, l2):
    cur1 = l1.head
    cur2 = l2.head

    while cur1 is not None and cur2 is not None:
        if cur1.value > cur2.value:
            return 1
        elif cur1.value < cur2.value:
            return -1
        cur1 = cur1.next
        cur2 = cur2.next

    if cur1 is not None:
        return 1
    elif cur2 is not None:
        return -1
    else:
        return 0

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            return

        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = node

    def traverse_print(self):
        cur = self.head
        while cur.next is not None:
            print(cur.value)
            cur = cur.next


l1 = LinkedList()
l1.add("g")
l1.add("e")
l1.add("e")
l1.add("k")
l1.add("s")
l1.add("a")
l2 = LinkedList()
l2.add("g")
l2.add("e")
l2.add("e")
l2.add("k")
l2.add("s")
l2.add("a")
l2.add("b")

print(compare(l1, l2)) # -1

