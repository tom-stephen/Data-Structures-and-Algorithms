from mylib.datastructures.linear.SLL import SinglyLinkedList as SLL
from mylib.datastructures.nodes.Single_linked_Node import Node as SNode

def test_SLL():
    # test the circulat doubly linked list
    sll = SLL()

    # insert elements into the list
    for i in range(10):
        node = SNode(i)
        sll.insert(node, i)
    
    sll.print()

test_SLL()