from nodes.Doubly_linked_Node import Node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.sorted = False
        self.length = 0
    
    def __init__(self, node):
        self.head = node
        self.tail = node
        self.sorted = False
        self.length = 1

    def insertHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1
        self.sorted = False    
    
    def insertTail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1
        self.sorted = False
    
    def insert(self, node, value):
        if self.head is None:
            self.head = node
            self.tail = node
            self.length += 1
            self.sorted = False
            return
        
        if self.head.value == value:
            self.insertHead(node)
            return
        
        current_node = self.head
        while current_node.next is not None:
            if current_node.value == value:
                node.next = current_node.next
                current_node.next.prev = node
                current_node.next = node
                node.prev = current_node
                self.length += 1
                self.sorted = False
                return
            current_node = current_node.next
        
        if current_node.value == value:
            self.insertTail(node)
            return
        
    def sort(self):
        if self.head is None:
            return
        
        current_node = self.head
        while current_node.next is not None:
            if current_node.value > current_node.next.value:
                temp = current_node.value
                current_node.value = current_node.next.value
                current_node.next.value = temp
            current_node = current_node.next
        self.sorted = True

    def sortedInsert(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            self.length += 1
            self.sorted = True
            return
        
        # check if the list is sorted
        current_node = self.head
        while current_node.next is not None:
            if current_node.value > current_node.next.value:
                self.sort()
                break
            current_node = current_node.next
        
        # insert the node
        if node.value < self.head.value:
            self.insertHead(node)
            self.sorted = True
            return
        elif node.value > self.tail.value:
            self.insertTail(node)
            self.sorted = True
            return
        
        current_node = self.head
        while current_node.next is not None:
            if current_node.value < node.value and current_node.next.value > node.value:
                node.next = current_node.next
                current_node.next.prev = node
                current_node.next = node
                node.prev = current_node
                self.length += 1
                self.sorted = True
                return
            current_node = current_node.next

    def Search(self, value):
        if self.head is None:
            return None
        
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return current_node
            current_node = current_node.next
        return None
    
    def DeleteHead(self):
        if self.head is None:
            return None
        
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1

    def DeleteTail(self):
        if self.head is None:
            return None
        
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1

    def Delete(self, node):
        if self.head is None:
            return None
        
        if self.head == node:
            self.DeleteHead()
            return
        
        if self.tail == node:
            self.DeleteTail()
            return
        
        current_node = self.head
        while current_node is not None:
            if current_node == node:
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
                self.length -= 1
                return
            current_node = current_node.next

    def Clear(self):
        self.head = None
        self.tail = None
        self.sorted = False
        self.length = 0
    
    def Print(self):
        # print the length, sorted status, and values of the list
        print('Length: ' + str(self.length))
        print('Sorted: ' + str(self.sorted))
        print('Values: ', end='')
        if self.head is None:
            print('None')
            return
        
        current_node = self.head
        while current_node.next is not None:
            print(current_node.value, end=' ')
            current_node = current_node.next
        print(current_node.value)
    





    # def add_node(self, value):
    #     new_node = Node(value)
    #     if self.length == 0:
    #         self.head = new_node
    #         self.tail = new_node
    #     else:
    #         new_node.prev = self.tail
    #         self.tail.next = new_node
    #         self.tail = new_node
    #     self.length += 1
    
    # def remove_node(self, value):
    #     if self.length == 0:
    #         raise ValueError('Cannot remove from empty list.')
    #     if self.head.value == value:
    #         if self.length == 1:
    #             self.head = None
    #             self.tail = None
    #         else:
    #             self.head = self.head.next
    #             self.head.prev = None
    #         self.length -= 1
    #         return
    #     current_node = self.head
    #     while current_node.next is not None:
    #         if current_node.next.value == value:
    #             if current_node.next.next is not None:
    #                 current_node.next.next.prev = current_node
    #             else:
    #                 self.tail = current_node
    #             current_node.next = current_node.next.next
    #             self.length -= 1
    #             return
    #         current_node = current_node.next
    #     raise ValueError('Value not found in list.')
    
    # def __len__(self):
    #     return self.length
    
    # def __str__(self):
        if self.length == 0:
            return '[]'
        current_node = self.head
        output = '['
        while current_node is not None:
            output += str(current_node.value) + ', '
            current_node = current_node.next
        return output[:-2] + ']'
