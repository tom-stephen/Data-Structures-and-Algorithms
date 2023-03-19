from nodes.Doubly_linked_Node import Node

class CircularDoublyLinkedList:
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
            self.head.prev = self.tail
        else:
            new_node.next = self.head
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.head.prev = self.tail
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
                self.head.prev = self.tail
            self.length -= 1
            return
        current_node = self.head
        while current_node.next is not self.head:
            if current_node.next.value == value:
                if current_node.next is self.tail:
                    self.tail = current_node
                current_node.next = current_node.next.next
                current_node.next.prev = current_node
                self.length -= 1
                return
            current_node = current_node.next
        raise ValueError('Value not found in list.')
    
    def peek(self):
        if self.length == 0:
            raise ValueError('Cannot peek from empty list.')
        return self.head.value
    
    def remove(self):
        if self.length == 0:
            raise ValueError('Cannot remove from empty list.')
        value = self.head.value
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            self.head = self.head.next
            self.tail.next = self.head
            self.head.prev = self.tail
        self.length -= 1
        return value
    
    def is_empty(self):
        return self.length == 0
    
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