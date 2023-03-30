from nodes.Doubly_linked_Node import Node

# NOTE: i dont know if this needs to have a max size or not. if there is then this will need to be changed

class CircularDoublyLinkedList:

    def __init__(self, node=None):
        if node is None:
            self.head = None
            self.tail = None
            self.sorted = False
            self.length = 0
            return
        else:
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

    def insert(self, node, index):
        if index == 0:
            self.insertHead(node)
            return
        elif index == self.length:
            self.insertTail(node)
            return
        
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        node.next = current_node
        node.prev = current_node.prev
        current_node.prev.next = node
        current_node.prev = node
        self.length += 1
        self.sorted = False

    def sort(self):
        if self.head is None:
            return
        
        if self.sorted:
            return  
        
        for i in range(self.length):
            current_node = self.head
            for j in range(self.length):
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
        
        if self.sorted:
            if node.value < self.head.value:
                self.insertHead(node)
                return
            elif node.value > self.tail.value:
                self.insertTail(node)
                return
            else:
                current_node = self.head
                while current_node.next is not None:
                    if current_node.value < node.value and current_node.next.value > node.value:
                        node.next = current_node.next
                        node.prev = current_node
                        current_node.next.prev = node
                        current_node.next = node
                        self.length += 1
                        self.sorted = True
                        return
                    current_node = current_node.next
        else:
            self.insertTail(node)
            self.sort()

    def Search(self, node):
        if self.head is None:
            return None
        
        current_node = self.head
        while current_node is not None:
            if current_node.value == node.value:
                return current_node
            current_node = current_node.next
        return None
    
    def deleteHead(self):
        if self.head is None:
            return None
        
        if self.head.next is None:
            self.head = None
            self.tail = None
            self.length -= 1
            return
        
        self.head = self.head.next
        self.head.prev = None
        self.length -= 1

    def deleteTail(self):
        if self.head is None:
            return None
        
        if self.head.next is None:
            self.head = None
            self.tail = None
            self.length -= 1
            return
        
        self.tail = self.tail.prev
        self.tail.next = None
        self.length -= 1

    def delete(self, node):
        if self.head is None:
            return None
        
        if self.head.value == node.value:
            self.DeleteHead()
            return
        
        if self.tail.value == node.value:
            self.DeleteTail()
            return
        
        current_node = self.head
        while current_node is not None:
            if current_node.value == node.value:
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
                self.length -= 1
                return
            current_node = current_node.next

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0
        self.sorted = False

    def print(self):
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


        if self.length == 0:
            return '[]'
        current_node = self.head
        output = '['
        while current_node is not self.tail:
            output += str(current_node.value) + ', '
            current_node = current_node.next
        output += str(self.tail.value) + ']'
        return output