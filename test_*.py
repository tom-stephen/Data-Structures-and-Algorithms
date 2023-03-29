# Testing file for testing all algorithm implementations

import numpy as np
import matplotlib.pyplot as plt
import pytest

import mylib.datastructures.heap.VBH_Max as MaxHeap
def test_VBH_Max():
    # create a max heap object
    max_heap = MaxHeap()

    # add elements to the heap
    max_heap.insert(10)
    max_heap.insert(20)
    max_heap.insert(15)

    # test that the maximum element is returned correctly
    assert max_heap.peek() == 20

    # test the extract max method
    assert max_heap.extract_max() == 20

    # test the size method
    assert max_heap.size() == 2

    # insert more numbers
    max_heap.insert(30)
    max_heap.insert(25)
    max_heap.insert(5)

    # test that the size method returns the correct size
    assert max_heap.size() == 5

    # test the heapsort method for a max heap
    arr = [10, 20, 15, 30, 25, 5]
    assert MaxHeap.heapsort(arr) == [30, 25, 20, 15, 10, 5]

    # test that elements are removed in the correct order
    assert max_heap.remove() == 30
    assert max_heap.remove() == 25
    assert max_heap.remove() == 15
    assert max_heap.remove() == 10
    assert max_heap.remove() == 5

    # test that the heap is empty after removing all elements
    assert max_heap.is_empty() == True

# This needs to be changed
import mylib.datastructures.heap.VBH_Min as MinHeap
def test_VBH_Min():
    # create a min heap object
    min_heap = MinHeap()

    # add elements to the heap
    min_heap.insert(10)
    min_heap.insert(20)
    min_heap.insert(15)

    # test that the minimum element is returned correctly
    assert min_heap.peek() == 10

    # test the extract min method
    assert min_heap.extract_min() == 10

    # test the size method
    assert min_heap.size() == 2

    # insert more numbers
    min_heap.insert(30)
    min_heap.insert(25)
    min_heap.insert(5)

    # test that the size method returns the correct size
    assert min_heap.size() == 5

    # test the heapsort method for a min heap
    arr = [10, 20, 15, 30, 25, 5]
    assert MinHeap.heapsort(arr) == [5, 10, 15, 20, 25, 30]

    # test that elements are removed in the correct order
    assert min_heap.remove() == 5
    assert min_heap.remove() == 15
    assert min_heap.remove() == 20
    assert min_heap.remove() == 25
    assert min_heap.remove() == 30

    # test that the heap is empty after removing all elements
    assert min_heap.is_empty() == True

# This needs to be changed
import mylib.datastructures.linear.CDLL as CDLL
def test_CDLL():
    # test the circulat doubly linked list
    cdll = CDLL()

    # insert elements into the list
    cdll.add_node(10)
    cdll.add_node(20)
    cdll.add_node(30)
    cdll.add_node(40)
    cdll.add_node(25)
    cdll.add_node(15)

    # test the remove node method
    cdll.remove_node(10)
    cdll.__len__ == 5
    cdll.remove_node(15)
    cdll.__len__ == 4
    cdll.remove_node(25)
    cdll.__len__ == 3
    cdll.remove_node(30)
    cdll.__len__ == 2
    cdll.remove_node(40)
    cdll.__len__ == 1
    cdll.remove_node(20)
    cdll.__len__ == 0

    # test the add node method
    cdll.add_node(10)
    cdll.add_node(20)
    cdll.add_node(30)
    cdll.add_node(40)
    cdll.add_node(25)
    cdll.add_node(15)
    
    # test the peek
    assert cdll.peek() == 10

    # test the remove method
    assert cdll.remove() == 10
    assert cdll.remove() == 20
    assert cdll.remove() == 30
    assert cdll.remove() == 40
    assert cdll.remove() == 25
    assert cdll.remove() == 15

    # test the is empty method
    assert cdll.is_empty() == True

# i think this is implemented but this needs to be CHECKED
import mylib.datastructures.linear.DLL as DLL
def test_DLL():
    from mylib.datastructures.nodes.Doubly_linked_Node import Node
    from mylib.datastructures.linear.DLL import DoublyLinkedList


    def insertHead_test():
        dll = DoublyLinkedList()
        node1 = Node(1)
        node2 = Node(2)
        dll.insertHead(node1)
        dll.insertHead(node2)
        assert dll.head == node2
        assert dll.tail == node1
        assert dll.length == 2


    def insertTail_test():
        dll = DoublyLinkedList()
        node1 = Node(1)
        node2 = Node(2)
        dll.insertTail(node1)
        dll.insertTail(node2)
        assert dll.head == node1
        assert dll.tail == node2
        assert dll.length == 2


    def insert_test():
        dll = DoublyLinkedList()
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        dll.insertTail(node1)
        dll.insertTail(node3)
        dll.insert(node2, 1)
        assert dll.head == node1
        assert dll.tail == node3
        assert dll.length == 3


    def sort_test():
        dll = DoublyLinkedList()
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        dll.insertTail(node3)
        dll.insertTail(node1)
        dll.insertTail(node2)
        dll.sort()
        assert dll.head == node1
        assert dll.tail == node3


    def sortedInsert_test():
        dll = DoublyLinkedList()
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        dll.sortedInsert(node3)
        dll.sortedInsert(node1)
        dll.sortedInsert(node2)
        assert dll.head == node1
        assert dll.tail == node3
        assert dll.length == 3


    def search_test():
        dll = DoublyLinkedList()
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        dll.insertTail(node1)
        dll.insertTail(node2)
        dll.insertTail(node3)
        assert dll.search(2) == node2
        assert dll.search(4) is None


    def deleteHead_test():
        dll = DoublyLinkedList()
        node1 = Node(1)
        node2 = Node(2)
        dll.insertTail(node1)
        dll.insertTail(node2)
        dll.deleteHead()
        assert dll.head == node2
        assert dll.tail == node2
        assert dll.length == 1


    def deleteTail_test():
        dll = DoublyLinkedList()
        node1 = Node(1)
        node2 = Node(2)
        dll.insertTail(node1)
        dll.insertTail(node2)
        dll.deleteTail()
        assert dll.head == node1
        assert dll.tail == node1
        assert dll.length == 1


    def delete_test():
        dll = DoublyLinkedList()
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        dll.insertTail

    # run the tests above
    insertHead_test()
    insertTail_test()
    insert_test()
    sort_test()
    sortedInsert_test()
    search_test()
    deleteHead_test()
    deleteTail_test()
    delete_test()


# i think this is implemented but this needs to be CHECKED
import mylib.datastructures.linear.SLL as SLL
def test_SLL():
    from mylib.datastructures.nodes.Single_linked_Node import Node
    from mylib.datastructures.linear.SLL import SinglyLinkedList

    # Test the insertHead() method
    linked_list = SinglyLinkedList()
    linked_list.insertHead(Node(1))
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 1
    assert linked_list.length == 1

    linked_list.insertHead(Node(2))
    assert linked_list.head.value == 2
    assert linked_list.tail.value == 1
    assert linked_list.length == 2

    # Test the insertTail() method
    linked_list = SinglyLinkedList()
    linked_list.insertTail(Node(1))
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 1
    assert linked_list.length == 1

    linked_list.insertTail(Node(2))
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 2
    assert linked_list.length == 2

    # Test the insert() method
    linked_list = SinglyLinkedList()
    linked_list.insert(Node(1), 0)
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 1
    assert linked_list.length == 1

    linked_list.insert(Node(2), 1)
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 2
    assert linked_list.length == 2

    linked_list.insert(Node(3), 1)
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 2
    assert linked_list.length == 3

    # Test the sort() method
    linked_list = SinglyLinkedList()
    linked_list.insertHead(Node(2))
    linked_list.insertHead(Node(1))
    linked_list.insertTail(Node(4))
    linked_list.insertTail(Node(3))
    linked_list.sort()
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 4
    assert linked_list.length == 4

    # Test the sortedInsert() method
    linked_list = SinglyLinkedList()
    linked_list.sortedInsert(Node(2))
    assert linked_list.head.value == 2
    assert linked_list.tail.value == 2
    assert linked_list.length == 1

    linked_list.sortedInsert(Node(1))
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 2
    assert linked_list.length == 2

    linked_list.sortedInsert(Node(3))
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 3
    assert linked_list.length == 3

    # Test the search() method
    linked_list = SinglyLinkedList()
    linked_list.insertTail(Node(1))
    linked_list.insertTail(Node(2))
    linked_list.insertTail(Node(3))
    assert linked_list.search(Node(2)).value == 2
    assert linked_list.search(Node(4)) is None

    # Test the deleteHead() method
    linked_list = SinglyLinkedList()
    linked_list.insertTail(Node(1))
    linked_list.insertTail(Node(2))
    linked_list.insertTail(Node(3))
    assert linked_list.deleteHead() == 1
    assert linked_list.head.value == 2
    assert linked_list.tail.value == 3
    assert linked_list.length == 2

    # Test the deleteTail() method
    linked_list = SinglyLinkedList()
    linked_list.insertTail(Node(1))
    linked_list.insertTail(Node(2))
    linked_list.insertTail(Node(3))
    assert linked_list.deleteTail() == 3
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 2
    assert linked_list.length == 2

    # Test the delete() method
    linked_list = SinglyLinkedList()
    linked_list.insertTail(Node(1)) 
    linked_list.insertTail(Node(2))
    linked_list.insertTail(Node(3))
    assert linked_list.delete(Node(2)) == 2
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 3
    assert linked_list.length == 2


# This needs to be changed
import mylib.datastructures.linear.CSLL as CSLL
def test_CSLL():
    # test the circular singly linked list
    csll = CSLL()

    # insert elements into the list
    csll.add_node(10)
    csll.add_node(20)
    csll.add_node(30)
    csll.add_node(40)
    csll.add_node(25)
    csll.add_node(15)

    # test the remove node method
    csll.remove_node(10)
    csll.__len__ == 5
    csll.remove_node(15)
    csll.__len__ == 4
    csll.remove_node(25)
    csll.__len__ == 3
    csll.remove_node(30)
    csll.__len__ == 2
    csll.remove_node(40)
    csll.__len__ == 1
    csll.remove_node(20)
    csll.__len__ == 0

    # test the add node method
    csll.add_node(10)
    csll.add_node(20)
    csll.add_node(30)
    csll.add_node(40)
    csll.add_node(25)
    csll.add_node(15)
    
    # test the peek
    assert csll.peek() == 10

    # test get_node
    assert csll.get_node(0).data == 10

    # test the remove method
    assert csll.remove() == 10
    assert csll.remove() == 20
    assert csll.remove() == 30
    assert csll.remove() == 40
    assert csll.remove() == 25
    assert csll.remove() == 15

    # test the is empty method
    assert csll.is_empty() == True

# This needs to be changed
import mylib.datastructures.linear.Stack as STACK
def test_STACK():
    # test the stack
    stack = STACK()

    # test the push method
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(25)
    stack.push(15)

    # test the peek
    assert stack.peek() == 15

    # test the pop method
    assert stack.pop() == 15

    # test the peek
    assert stack.peek() == 25

    # remove rest of items
    assert stack.pop() == 25
    assert stack.pop() == 40
    assert stack.pop() == 30
    assert stack.pop() == 20
    assert stack.pop() == 10

    # test the is empty method
    assert stack.is_empty() == True

# This needs to be changed
import mylib.datastructures.linear.Queue as QUEUE
def test_QUEUE():
    # test the queue
    queue = QUEUE()

    # test the enqueue method
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(25)
    queue.enqueue(15)

    # test the size
    assert queue.size() == 6

    # test the peek
    assert queue.peek() == 10

    # test the dequeue method
    assert queue.dequeue() == 10
    assert queue.dequeue() == 20
    assert queue.dequeue() == 30
    assert queue.dequeue() == 40
    assert queue.dequeue() == 25
    assert queue.dequeue() == 15

    # test the is empty method
    assert queue.is_empty() == True