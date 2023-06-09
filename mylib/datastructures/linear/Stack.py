from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.parent))

from mylib.datastructures.linear.SLL import SinglyLinkedList


class Stack (SinglyLinkedList):

    def __init__(self, head=None):
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
    
    def print(self):
        print('length: ', self.length)
        print('Values: ', end='')
        if self.head is None:
            print('None')
            return
        
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next
        
