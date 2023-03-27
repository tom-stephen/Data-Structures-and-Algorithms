from nodes.Single_linked_Node import Node

# NOTE: i dont know if this needs to have a max size or not. if there is then this will need to be changed

class CircularLinkedList:
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
            self.head = node
        self.length += 1
        self.sorted = False

    def insertTail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
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
                current_node.next = node
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
            next_node = current_node.next
            while next_node is not None:
                if current_node.value > next_node.value:
                    temp = current_node.value
                    current_node.value = next_node.value
                    next_node.value = temp
                next_node = next_node.next
            current_node = current_node.next
        self.sorted = True

    def SortedInsert(self, node):
        # check if list is sorted
        if self.head is None:
            self.head = node
            self.tail = node
            self.length += 1
            return

        current_node = self.head
        while current_node.next is not None:
            if current_node.value > current_node.next.value:
                self.sort()
                break
            current_node = current_node.next

        # insert node
        if self.head.value > node.value:
            self.insertHead(node)
            self.sorted = True
            return
        
        current_node = self.head
        while current_node.next is not None:
            if current_node.value <= node.value and current_node.next.value >= node.value:
                node.next = current_node.next
                current_node.next = node
                self.length += 1
                self.sorted = True
                return
            current_node = current_node.next
        
        if current_node.value <= node.value:
            self.insertTail(node)
            self.sorted = True
            return
        
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
            return
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.length -= 1

    def DeleteTail(self):
        if self.head is None:
            return
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current_node = self.head
            while current_node.next is not self.tail:
                current_node = current_node.next
            current_node.next = None
            self.tail = current_node
        self.length -= 1

    def Delete(self, node):
        if self.head is None:
            return
        
        if self.head == node:
            self.DeleteHead()
            return
        
        if self.tail == node:
            self.DeleteTail()
            return
        
        current_node = self.head
        while current_node.next is not None:
            if current_node.next == node:
                current_node.next = current_node.next.next
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