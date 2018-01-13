class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        self.head = Node(value, next_node=self.head)

    def delete(self, value):
        current = self.head
        previous = None
        found = False
        while current and not found:
            if current.value == value:
                found = True
            else:
                previous = current
                current = current.next

        if found:
            if previous != None:
                previous.next = current.next
            else:
                self.head = current.next

    def to_list(self):
        array = []
        current = self.head
        while current != None:
            array.append(current.value)
            current = current.next
        return array

    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.next
        return count

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node
