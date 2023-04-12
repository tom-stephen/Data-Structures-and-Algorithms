from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.parent))

from mylib.datastructures.linear.SLL import SinglyLinkedList


class Queue(SinglyLinkedList):

    def __init__(self, head=None):
        super().__init__(head)

    def insertHead(self):
        pass

    def deleteTail(self):
        pass

    def sort(self):
        pass

    def insert(self, node, index):
        pass

    def sortedInsert(self, node):
        pass

    def enqueue(self, item):
        self.insertTail(item)

    def dequeue(self):
        return self.deleteHead()

    def size(self):
        return self.length
    
    def peek(self):
        if self.head is None:
            return None
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