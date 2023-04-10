# Testing file for testing all algorithm implementations


# import mylib.datastructures.heap.VBH_Max as MaxHeap
# def test_VBH_Max():
#     # create a max heap object
#     max_heap = MaxHeap()

#     # add elements to the heap
#     max_heap.insert(10)
#     max_heap.insert(20)
#     max_heap.insert(15)

#     # test that the maximum element is returned correctly
#     assert max_heap.peek() == 20

#     # test the extract max method
#     assert max_heap.extract_max() == 20

#     # test the size method
#     assert max_heap.size() == 2

#     # insert more numbers
#     max_heap.insert(30)
#     max_heap.insert(25)
#     max_heap.insert(5)

#     # test that the size method returns the correct size
#     assert max_heap.size() == 5

#     # test the heapsort method for a max heap
#     arr = [10, 20, 15, 30, 25, 5]
#     assert MaxHeap.heapsort(arr) == [30, 25, 20, 15, 10, 5]

#     # test that elements are removed in the correct order
#     assert max_heap.remove() == 30
#     assert max_heap.remove() == 25
#     assert max_heap.remove() == 15
#     assert max_heap.remove() == 10
#     assert max_heap.remove() == 5

#     # test that the heap is empty after removing all elements
#     assert max_heap.is_empty() == True

# # This needs to be changed
# import mylib.datastructures.heap.VBH_Min as MinHeap
# def test_VBH_Min():
#     # create a min heap object
#     min_heap = MinHeap()

#     # add elements to the heap
#     min_heap.insert(10)
#     min_heap.insert(20)
#     min_heap.insert(15)

#     # test that the minimum element is returned correctly
#     assert min_heap.peek() == 10

#     # test the extract min method
#     assert min_heap.extract_min() == 10

#     # test the size method
#     assert min_heap.size() == 2

#     # insert more numbers
#     min_heap.insert(30)
#     min_heap.insert(25)
#     min_heap.insert(5)

#     # test that the size method returns the correct size
#     assert min_heap.size() == 5

#     # test the heapsort method for a min heap
#     arr = [10, 20, 15, 30, 25, 5]
#     assert MinHeap.heapsort(arr) == [5, 10, 15, 20, 25, 30]

#     # test that elements are removed in the correct order
#     assert min_heap.remove() == 5
#     assert min_heap.remove() == 15
#     assert min_heap.remove() == 20
#     assert min_heap.remove() == 25
#     assert min_heap.remove() == 30

#     # test that the heap is empty after removing all elements
#     assert min_heap.is_empty() == True

# SORTING IS BROKEN
def test_CDLL():
    from mylib.datastructures.linear.CDLL import CircularDoublyLinkedList as CDLL
    from mylib.datastructures.nodes.Doubly_linked_Node import Node
    # create nodes
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    # create linked list and insert nodes
    linked_list = CDLL()
    linked_list.insertTail(node1)
    linked_list.insertTail(node2)
    linked_list.insertTail(node3)

    # test length and values
    assert linked_list.length == 3
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 3

    # test sorted insert
    linked_list.sortedInsert(node4)
    assert linked_list.length == 4
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 4

    # test delete
    linked_list.delete(node2)
    assert linked_list.length == 3
    assert linked_list.Search(node2) is None

    # test clear
    linked_list.clear()
    assert linked_list.length == 0
    assert linked_list.head is None
    assert linked_list.tail is None

# SORTING IS BROKEN
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
        assert dll.head.value == 1
        assert dll.tail.value == 3
        assert dll.length == 3
        assert dll.head.next.value == 2
        assert dll.tail.prev.value == 2


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
        dll.insertTail(node1)
        dll.insertTail(node2)
        dll.insertTail(node3)
        dll.delete(node2)
        assert dll.head == node1
        assert dll.tail == node3
        assert dll.length == 2

    # run the tests above
    insertHead_test()
    insertTail_test()
    insert_test()
    sort_test() ############################## this one is broken
    sortedInsert_test()
    search_test()
    deleteHead_test()
    deleteTail_test()
    delete_test()


# SORTING IS BROKEN
def test_SLL():
    from mylib.datastructures.nodes.Single_linked_Node import Node
    from mylib.datastructures.linear.SLL import SinglyLinkedList

    def one_test():
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

    def two_test():
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

    def three_test():
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

    def four_test():
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

    def five_test():
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

    def six_test():
        # Test the search() method
        linked_list = SinglyLinkedList()
        linked_list.insertTail(Node(1))
        linked_list.insertTail(Node(2))
        linked_list.insertTail(Node(3))
        assert linked_list.search(Node(2)).value == 2
        assert linked_list.search(Node(4)) is None

    def seven_test():
        # Test the deleteHead() method
        linked_list = SinglyLinkedList()
        linked_list.insertTail(Node(1))
        linked_list.insertTail(Node(2))
        linked_list.insertTail(Node(3))
        assert linked_list.deleteHead() == 1
        assert linked_list.head.value == 2
        assert linked_list.tail.value == 3
        assert linked_list.length == 2

    def eight_test():
        # Test the deleteTail() method
        linked_list = SinglyLinkedList()
        linked_list.insertTail(Node(1))
        linked_list.insertTail(Node(2))
        linked_list.insertTail(Node(3))
        assert linked_list.deleteTail() == 3
        assert linked_list.head.value == 1
        assert linked_list.tail.value == 2
        assert linked_list.length == 2

    def nine_test():
        # Test the delete() method
        linked_list = SinglyLinkedList()
        linked_list.insertTail(Node(1)) 
        linked_list.insertTail(Node(2))
        linked_list.insertTail(Node(3))
        assert linked_list.delete(Node(2)) == 2
        assert linked_list.head.value == 1
        assert linked_list.tail.value == 3
        assert linked_list.length == 2

    def sort_test():
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

    one_test()
    two_test()
    three_test()
    four_test()
    five_test()
    six_test()
    seven_test()
    eight_test()
    nine_test()
    sort_test()

# SORTING IS BROKEN
def test_CSLL():
    from mylib.datastructures.linear.CSLL import CircularLinkedList
    from mylib.datastructures.nodes.Single_linked_Node import Node
    # create nodes
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    # test inserting nodes
    cll = CircularLinkedList()
    cll.insertHead(node2)
    cll.insertTail(node1)
    cll.insert(node3, 1)

    # test sorting
    cll.sort()

    # test sorted insert
    node4 = Node(0)
    cll.sortedInsert(node4)

    # test search
    node = cll.search(node3)
    assert node == node3

    # test deleting nodes
    cll.deleteTail()
    cll.deleteHead()
    cll.delete(node3)

    # test clearing list
    cll.clear()
    assert cll.length == 0
    assert cll.head is None
    assert cll.tail is None
    assert not cll.sorted

    # test printing list
    cll.insertTail(node1)
    cll.insertTail(node2)
    cll.insertTail(node3)
    cll.print()

# Good but says that some tests where deselected???
def test_STACK():
    from mylib.datastructures.linear.Stack import Stack
    from mylib.datastructures.nodes.Single_linked_Node import Node
    # Create a new empty stack
    stack = Stack()

    # Test push method
    stack.push(Node(1))
    stack.push(Node(2))
    stack.push(Node(3))

    # Test pop method
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1

    # Test peek method
    stack.push(Node(4))
    stack.push(Node(5))
    assert stack.peek() == 5
    stack.pop()
    assert stack.peek() == 4

    # Test length and print methods
    stack.push(Node(6))
    assert stack.length == 2


# Good but says that some tests where deselected???
def test_QUEUE():
    from mylib.datastructures.linear.Queue import Queue
    from mylib.datastructures.nodes.Single_linked_Node import Node
    # Create a new queue
    q = Queue()

    # Enqueue some items
    q.enqueue(Node(1))
    q.enqueue(Node(2))
    q.enqueue(Node(3))

    # Check the size of the queue
    assert q.size() == 3

    # Check the first item in the queue
    assert q.peek() == 1

    # Dequeue an item and check its value
    assert q.dequeue() == 1

    # Check the size of the queue again
    assert q.size() == 2

    # Enqueue another item
    q.enqueue(Node(4))

    # Check the size of the queue again
    assert q.size() == 3

    # Dequeue all remaining items and check their values
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.dequeue() == 4

    # Check that the queue is now empty
    assert q.size() == 0
    assert q.peek() is None


def test_BST():
    from mylib.datastructures.trees.BST import BinarySearchTree as BST
    from mylib.datastructures.nodes.Tree_Node import Node
    # Create a new empty BST
    bst = BST()

    # Test insert method
    bst.insert(Node(8))
    bst.insert(Node(5))
    bst.insert(Node(3))
    bst.insert(Node(7))
    bst.insert(Node(2))
    bst.insert(Node(4))
    bst.insert(Node(6))

    # Test search method
    assert bst.search(5).data == 5
    assert bst.search(3).data == 3
    assert bst.search(7).data == 7
    assert bst.search(2).data == 2
    assert bst.search(4).data == 4
    assert bst.search(6).data == 6
    assert bst.search(8).data == 8
    assert bst.search(1) is None

    # Test delete method
    bst.delete(5)
    assert bst.search(5) is None
    bst.delete(3)
    assert bst.search(3) is None
    bst.delete(7)
    assert bst.search(7) is None
    bst.delete(2)
    assert bst.search(2) is None
    bst.delete(4)
    assert bst.search(4) is None
    bst.delete(6)
    assert bst.search(6) is None
    bst.delete(8)
    assert bst.search(8) is None

    # Test print method
    bst.insert(Node(5))
    bst.insert(Node(3))
    bst.insert(Node(7))
    bst.insert(Node(2))
    bst.insert(Node(4))
    bst.insert(Node(6))
    bst.insert(Node(8))
    bst.printBF()

    # Test clear method
    # bst.clear()
    # assert bst.root is None