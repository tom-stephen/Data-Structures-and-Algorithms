class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    # print it out
    def __str__(self):
        return str(self.value)
