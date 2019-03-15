class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        tmp = Node(value)
        tmp.next = self.head
        self.head = tmp
        return self

    def size(self):
        cnt = 0
        cur = self.head
        while cur is not None:
            cnt += 1
            cur = cur.next
        return cnt

    def traverse_print(self):
        cur = self.head
        while cur is not None:
            print(cur.value)
            cur = cur.next

def add_same_size(a, b):
    r, carry = add_same_size_helper(a.head, b.head)
    if carry > 0:
        r.push(carry)
    return r

def add_same_size_helper(a, b):
    if a.next is None:
        r = LinkedList()
        carry = 0
    else:
        r, carry = add_same_size_helper(a.next, b.next)

    v = a.value + b.value + carry
    carry = v // 10
    r.push(v % 10)

    return r, carry

a = LinkedList().push(3).push(6).push(5)
b = LinkedList().push(2).push(4).push(8)

r = add_same_size(a, b)
r.traverse_print()
