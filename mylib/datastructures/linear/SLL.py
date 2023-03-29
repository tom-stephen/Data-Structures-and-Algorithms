from nodes.Single_linked_Node import Node

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.sorted = False
        self.length = 0
    
    # Overload constructor with a Node object argument to use as head
    def __init__(self, head):
        self.head = head
        self.tail = head
        self.sorted = False
        self.length = 1

    def insertHead(self, node):
        node.next = self.head
        self.head = node
        self.length += 1
        self.sorted = False
    
    def insertTail(self, node):
        self.tail.next = node
        self.tail = node
        self.length += 1
        self.sorted = False

    def insert(self, node, index):
        if index == 0:
            self.insertHead(node)
        elif index == self.length:
            self.insertTail(node)
        else:
            current_node = self.head
            for i in range(index - 1):
                current_node = current_node.next
            node.next = current_node.next
            current_node.next = node
            self.length += 1
            self.sorted = False

    def sort(self):
        current = self.head
        if current is None:
            return
        
        while current.next is not None:
            next_node = current.next

            while next_node is not None:
                if current.value > next_node.value:
                    temp = current.value
                    current.value = next_node.value
                    next_node.value = temp
                next_node = next_node.next
            current = current.next
        self.sorted = True
    
    def sortedInsert(self, node):
        # must check if listed is sorted first. if it is not, then call sort()
        if self.head is None:
            self.head = node
            self.tail = node
            self.length += 1
            self.sorted = True
            return
        
        # check if the list is sorted
        current = self.head
        while current.next is not None:
            if current.value > current.next.value:
                self.sort()
                break
            current = current.next

        # insert the node
        if node.value < self.head.value:
            self.insertHead(node)
            self.sorted = True
            return
        
        if node.value > self.tail.value:
            self.insertTail(node)
            self.sorted = True
            return
        
        current_node = self.head
        while current_node.next is not None:
            if current_node.value < node.value and current_node.next.value > node.value:
                node.next = current_node.next
                current_node.next = node
                self.length += 1
                self.sorted = True
                return
            current_node = current_node.next  

    def search(self, node):
        current_node = self.head
        while current_node is not None:
            if current_node.value == node.value:
                return current_node
            current_node = current_node.next
        return None
    
    def deleteHead(self):
        if self.head is None:
            return None
        # return the value of the deleted node
        deleted_node = self.head
        self.head = self.head.next
        self.length -= 1
        return deleted_node.value
    
    def deleteTail(self):
        if self.head is None:
            return None
        
        if self.head.next is None:
            self.head = None
            return None
        
        current_node = self.head
        while current_node.next.next is not None:
            current_node = current_node.next
        # return the value of the deleted node
        deleted_node = current_node.next
        current_node.next = None
        self.length -= 1
        return deleted_node.value

    def delete(self, node):
        if self.head is None:
            return
        
        if self.head.value == node.value:
            self.DeleteHead()
            return
        
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.value == node.value:
                current_node.next = current_node.next.next
                self.length -= 1
                return
            current_node = current_node.next

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0
    
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
    