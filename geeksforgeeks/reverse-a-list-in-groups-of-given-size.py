class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None
    
    def add(self, value):
        node = self.Node(value)

        if self.head is None:
            self.head = node
            return

        temp = self.head
        self.head = node
        self.head.next = temp
        return

    # def reverse(self):
    #     cur = self.head
    #     prev_node = None

    #     while cur is not None:
    #         next_node = cur.next
    #         cur.next = prev_node

    #         prev_node = cur
    #         cur = next_node

    #     self.head, self.tail = self.tail, self.head

    def reverse_every(self, k):
        cur = self.head
        head = cur
        tail = None
        cnt = 0
        prev= 0

        while cur is not None:
            next_node = cur.next
            cur.next = prev

            prev = cur
            cur = next_node

            cnt += 1
            if cnt == k or cur is None:
                if tail is not None:
                    tail.next = prev
                else:
                    self.head = prev

                tail = head
                head = cur
                prev=None
                cnt = 0

    def to_array(self):
        arr = []

        cur = self.head
        while cur is not None:
            arr.append(cur.value)
            cur = cur.next

        return arr


a = LinkedList()
cur = a.head
for i in range(8, 0, -1):
    a.add(i)
print(a.to_array())


# a.reverse()
# print(a.to_array())

# a.reverse_every(3)
# print(a.to_array()) # 3->2->1->6->5->4->8->7

a.reverse_every(5)
print(a.to_array()) # 5->4->3->2->1->8->7->6
