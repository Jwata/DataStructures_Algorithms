class SkipList:
    def __init__(self):
        self.head = SkipNode()

    def update_list(self, value):
        next_length = len(self.head.next)
        update = [None] * next_length
        x = self.head

        for i in reversed(range(next_length)):
            while x.next[i] != None and x.next[i].value < value:
                x = x.next[i]
            update[i] = x

        return update

class SkipNode:
    def __init__(self, height = 0, value = None):
        self.value = value
        self.next = [None] * height
