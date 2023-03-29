from SLL import SinglyLinkedList


class Stack (SinglyLinkedList):
    def __init__(self):
        super().__init__()

    def __init__(self, head):
        super().__init__(head)

    def deleteTail(self):
        pass

    def sort(self):
        pass

    def insertTail(self, node):
        pass

    def insert(self, node, index):
        pass

    def sortedInsert(self, node):
        pass

    def push(self, node):
        self.insertHead(node)
    
    def pop(self):
        return self.deleteHead()
    
    def peek(self):
        return self.head.value
    
    def Print(self):
        print('length: ', self.length)
        print('sorted: ', self.sorted)
        print('Values: ', end='')
        if self.head is None:
            print('None')
            return
        
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next
        
