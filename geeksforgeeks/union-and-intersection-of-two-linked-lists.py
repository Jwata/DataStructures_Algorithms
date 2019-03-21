class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None

    def add_left(self, value):
        node = self.Node(value)

        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def to_array(self):
        arr = []

        cur = self.head
        while cur is not None:
            arr.append(cur.value)
            cur = cur.next

        return arr

# list1: 10->15->4->20
a = LinkedList()
a.add_left(20)
a.add_left(4)
a.add_left(15)
a.add_left(10)
print(a.to_array())

# list2:  8->4->2->10
b = LinkedList()
b.add_left(10)
b.add_left(2)
b.add_left(4)
b.add_left(8)
print(b.to_array())

def find_union_and_intersection(a, b):
    union = set()
    inter = set()

    cur_a = a.head
    while cur_a is not None:
        union.add(cur_a.value)
        cur_a = cur_a.next

    cur_b = b.head
    buf = set()
    while cur_b is not None:
        if cur_b.value in union:
            inter.add(cur_b.value)
        buf.add(cur_b.value)
        cur_b = cur_b.next


    union = merge_set(union, buf)

    union_list = LinkedList()
    union_list = add_set_to_list(union_list, union)

    inter_list = LinkedList()
    inter_list = add_set_to_list(inter_list, inter)

    return union_list, inter_list

def merge_set(a, b):
    for i in b:
        a.add(i)
    return a

def add_set_to_list(ll, s):
    for i in s:
        ll.add_left(i)
    return ll

union, inter = find_union_and_intersection(a, b)
print(union.to_array())
print(inter.to_array())

