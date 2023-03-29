# Testing file for testing all algorithm implementations

import numpy as np
import matplotlib.pyplot as plt
import pytest

from node.Doubly_linked_Node import Node as DNode
from node.Singly_linked_Node import Node as SNode
from node.Tree_Node import Node as TNode

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

import mylib.datastructures.linear.CDLL as CDLL
def test_CDLL():
    # test the circulat doubly linked list
    cdll = CDLL()

    # insert elements into the list
    for i in range(10):
        node = DNode(i)
        cdll.insert(node, i)
    
    # check to see if length is correct
    assert cdll.length == 10

    # test the insertHead method
    node = DNode(10)
    cdll.insertHead(node)
    assert cdll.head.value == 10

    # test the insertTail method
    node = DNode(11)
    cdll.insertTail(node)
    assert cdll.tail.value == 11

    # test the deleteHead method
    cdll.deleteHead()
    assert cdll.head.value == 0

    # test the deleteTail method
    cdll.deleteTail()
    assert cdll.tail.value == 9

    


import mylib.datastructures.linear.DLL as DLL
def test_DLL():
    # test the doubly linked list
    dll = DLL()

    # insert elements into the list
    dll.add_node(10)
    dll.add_node(20)
    dll.add_node(30)
    dll.add_node(40)
    dll.add_node(25)
    dll.add_node(15)

    # test the remove node method
    dll.remove_node(10)
    dll.__len__ == 5
    dll.remove_node(15)
    dll.__len__ == 4
    dll.remove_node(25)
    dll.__len__ == 3
    dll.remove_node(30)
    dll.__len__ == 2
    dll.remove_node(40)
    dll.__len__ == 1
    dll.remove_node(20)
    dll.__len__ == 0

    # test the add node method
    dll.add_node(10)
    dll.add_node(20)
    dll.add_node(30)
    dll.add_node(40)
    dll.add_node(25)
    dll.add_node(15)
    
    # test the peek
    assert dll.peek() == 10

    # test the remove method
    assert dll.remove() == 10
    assert dll.remove() == 20
    assert dll.remove() == 30
    assert dll.remove() == 40
    assert dll.remove() == 25
    assert dll.remove() == 15

    # test the is empty method
    assert dll.is_empty() == True

import mylib.datastructures.linear.SLL as SLL
def test_SLL():
    # test the singly linked list
    sll = SLL()

    # insert elements into the list
    sll.add_node(10)
    sll.add_node(20)
    sll.add_node(30)
    sll.add_node(40)
    sll.add_node(25)
    sll.add_node(15)

    # test the remove node method
    sll.remove_node(10)
    sll.__len__ == 5
    sll.remove_node(15)
    sll.__len__ == 4
    sll.remove_node(25)
    sll.__len__ == 3
    sll.remove_node(30)
    sll.__len__ == 2
    sll.remove_node(40)
    sll.__len__ == 1
    sll.remove_node(20)
    sll.__len__ == 0

    # test the add node method
    sll.add_node(10)
    sll.add_node(20)
    sll.add_node(30)
    sll.add_node(40)
    sll.add_node(25)
    sll.add_node(15)
    
    # test the peek
    assert sll.peek() == 10

    # test the remove method
    assert sll.remove() == 10
    assert sll.remove() == 20
    assert sll.remove() == 30
    assert sll.remove() == 40
    assert sll.remove() == 25
    assert sll.remove() == 15

    # test the is empty method
    assert sll.is_empty() == True

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