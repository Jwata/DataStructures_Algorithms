class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        elif self.head.value >= value:
            node.next = self.head
            self.head = node
            return

        cur = self.head
        while cur.next is not None and cur.next.value < value:
            cur = cur.next

        node.next = cur.next
        cur.next = node

    def traverse_print(self):
        cur = self.head
        while cur:
            print(cur.value)
            cur = cur.next


ll = LinkedList()

init_values = [5, 10, 7, 3, 1, 9]

for v in init_values:
    ll.insert(v)

ll.insert(9)

ll.traverse_print()  # sholud be 2, 5, 7, 9, 10, 15
# Time: O(n) Space: O(1)
