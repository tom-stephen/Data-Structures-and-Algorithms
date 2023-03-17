from nodes.Single_linked_Node import Node

class SinglyLinkedList:
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
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def remove_node(self, value):
        if self.length == 0:
            raise ValueError('Cannot remove from empty list.')
        if self.head.value == value:
            self.head = self.head.next
            self.length -= 1
            return
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.value == value:
                current_node.next = current_node.next.next
                if current_node.next is None:
                    self.tail = current_node
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