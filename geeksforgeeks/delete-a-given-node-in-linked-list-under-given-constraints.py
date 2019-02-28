class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def deleteNode(s, d):
    if s.value == d.value:
        if s.next == None:
            raise Exception("Linked List can't become empty.")

        s.value = s.next.value
        s.next = s.next.next
        return

    cur = s
    while cur.next is not None and cur.next.value != d.value:
        if cur.value == d.value:
            break
        cur = cur.next

    if cur.next == None:
        # node not found
        return

    cur.next = cur.next.next
    return

def printLinkedList(s):
    cur = s
    while cur is not None:
        print(cur.value)
        cur = cur.next

s = Node(10)
s.next = Node(20)
s.next.next = Node(30)
s.next.next.next = Node(40)

deleteNode(s, Node(10))
printLinkedList(s)
