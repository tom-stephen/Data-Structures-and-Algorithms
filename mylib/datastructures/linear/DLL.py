from nodes.Doubly_linked_Node import Node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def add_node(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
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
                self.head.prev = None
            self.length -= 1
            return
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.value == value:
                if current_node.next.next is not None:
                    current_node.next.next.prev = current_node
                else:
                    self.tail = current_node
                current_node.next = current_node.next.next
                self.length -= 1
                return
            current_node = current_node.next
        raise ValueError('Value not found in list.')
    
    def __len__(self):
        return self.length
    
    def __str__(self):
        if self.length == 0:
            return '[]'
        current_node = self.head
        output = '['
        while current_node is not None:
            output += str(current_node.value) + ', '
            current_node = current_node.next
        return output[:-2] + ']'
