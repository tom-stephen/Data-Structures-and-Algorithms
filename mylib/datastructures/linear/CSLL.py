from nodes.Single_linked_Node import Node

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def add_node(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def remove_node(self, value):
        if self.length == 0:
            raise ValueError('Cannot remove from empty list.')
        if self.head.value == value:
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
            self.length -= 1
            return
        current_node = self.head
        while current_node.next is not self.head:
            if current_node.next.value == value:
                if current_node.next is self.tail:
                    self.tail = current_node
                current_node.next = current_node.next.next
                self.length -= 1
                return
            current_node = current_node.next
        raise ValueError('Value not found in list.')
    
    def peek(self):
        if self.length == 0:
            raise ValueError('Cannot peek from empty list.')
        return self.head.value
    
    def get_node(self, index):
        if index >= self.length:
            raise IndexError('Index out of range.')
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node

    def __len__(self):
        return self.length
    
    def __str__(self):
        if self.length == 0:
            return '[]'
        current_node = self.head
        output = '['
        while current_node is not self.tail:
            output += str(current_node.value) + ', '
            current_node = current_node.next
        output += str(self.tail.value) + ']'
        return output
    
