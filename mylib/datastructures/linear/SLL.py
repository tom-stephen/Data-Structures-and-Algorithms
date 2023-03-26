from nodes.Single_linked_Node import Node

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    # Overload constructor with a Node object argument to use as head
    def __init__(self, head):
        self.head = head
        self.tail = head
        self.length = 1

    def insertHead(self, node):
        node.next = self.head
        self.head = node
        self.length += 1
    
    def insertTail(self, node):
        self.tail.next = node
        self.tail = node
        self.length += 1

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
    
    def SortedInsert(self, node):
        # must check if listed is sorted first. if it is not, then call sort()
        if self.head is None:
            self.head = node
            self.tail = node
            self.length += 1
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
            return
        
        if node.value > self.tail.value:
            self.insertTail(node)
            return
        
        current = self.head
        while current.next is not None:
            if node.value < current.value:
                self.insertHead(node)
                return
            elif node.value > current.value and node.value < current.next.value:
                self.insert(node, current.value)
                return
            current = current.next    

    def Search(self, node):
        current_node = self.head
        while current_node is not None:
            if current_node.value == node.value:
                return current_node
            current_node = current_node.next
        return None
    
    def DeleteHead(self):
        if self.head is None:
            return
        self.head = self.head.next
        self.length -= 1
    
    def DeleteTail(self):
        if self.head is None:
            return
        
        if self.head.next is None:
            self.head = None
            return
        
        current_node = self.head
        while current_node.next.next is not None:
            current_node = current_node.next
        current_node.next = None
        self.length -= 1

    def Delete(self, node):
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

    def Clear(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def Print(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next
    