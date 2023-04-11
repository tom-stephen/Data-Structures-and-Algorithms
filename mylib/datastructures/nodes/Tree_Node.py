class Node:
    def __init__(self, data, balance=0, parent=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.balance = balance

    def __str__(self):
        return str(self.data)