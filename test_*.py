
# DONE
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

    #test the insertHead method
    node5 = Node(5)
    linked_list.insertHead(node5)
    assert linked_list.length == 5
    assert linked_list.head.value == 5
    assert linked_list.tail.value == 4

    # test the insert method
    node6 = Node(6)
    linked_list.insert(node6, 2)
    assert linked_list.length == 6
    assert linked_list.head.value == 5
    assert linked_list.tail.value == 4
    assert linked_list.Search(node6).value == 6

    # test delete
    linked_list.delete(node6)
    assert linked_list.length == 5
    assert linked_list.head.value == 5
    assert linked_list.tail.value == 4
    assert linked_list.Search(node6) is None

    #test delete tail
    linked_list.deleteTail()
    assert linked_list.length == 4
    assert linked_list.head.value == 5
    assert linked_list.tail.value == 3

    #test delete head
    linked_list.deleteHead()
    assert linked_list.length == 3
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 3

    # test search
    assert linked_list.Search(node2).value == 2

    #test the sort method
    linked_list.insertHead(node4)
    linked_list.insertHead(node6)
    linked_list.sort()
    assert linked_list.length == 5
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 6


    # test clear
    linked_list.clear()
    assert linked_list.length == 0
    assert linked_list.head is None
    assert linked_list.tail is None

# DONE
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

    def clear_test():
        dll = DoublyLinkedList()
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        dll.insertTail(node1)
        dll.insertTail(node2)
        dll.insertTail(node3)
        dll.clear()
        assert dll.head is None
        assert dll.tail is None
        assert dll.length == 0

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
    clear_test()

# DONE
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
        linked_list.sortedInsert(Node(0))
        assert linked_list.head.value == 0

    def deleteHead_test():
        # Test the deleteHead() method
        linked_list = SinglyLinkedList()
        linked_list.insertTail(Node(1))
        linked_list.insertTail(Node(2))
        linked_list.insertTail(Node(3))
        assert linked_list.deleteHead() == 1
        assert linked_list.head.value == 2
        assert linked_list.tail.value == 3
        assert linked_list.length == 2
    
    def deleteHead_test():
        # Test the deleteHead() method
        linked_list = SinglyLinkedList()
        linked_list.insertTail(Node(1))
        linked_list.insertTail(Node(2))
        linked_list.insertTail(Node(3))
        assert linked_list.deleteHead() == 1
        assert linked_list.head.value == 2
        assert linked_list.tail.value == 3
        assert linked_list.length == 2

    def clear_test():
        # Test the clear() method
        linked_list = SinglyLinkedList()
        linked_list.insertTail(Node(1))
        linked_list.insertTail(Node(2))
        linked_list.insertTail(Node(3))
        linked_list.clear()
        assert linked_list.head is None
        assert linked_list.tail is None
        assert linked_list.length == 0

    def delete_test():
        # Test the delete() method
        linked_list = SinglyLinkedList()
        linked_list.insertTail(Node(1))
        linked_list.insertTail(Node(2))
        linked_list.insertTail(Node(3))
        assert linked_list.delete(Node(2)) == 2
        assert linked_list.head.value == 1
        assert linked_list.tail.value == 3
        assert linked_list.length == 2


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
    deleteHead_test()
    deleteHead_test()
    clear_test()
    delete_test()

# DONE
def test_CSLL():
    from mylib.datastructures.linear.CSLL import CircularLinkedList
    from mylib.datastructures.nodes.Single_linked_Node import Node
    def insertHead_test():
        # Test the insertHead() method
        circular_linked_list = CircularLinkedList()
        circular_linked_list.insertHead(Node(1))
        circular_linked_list.insertHead(Node(2))
        circular_linked_list.insertHead(Node(3))
        assert circular_linked_list.head.value == 3
        assert circular_linked_list.tail.value == 1
        assert circular_linked_list.length == 3
    
    def insertTail_test():
        # Test the insertTail() method
        circular_linked_list = CircularLinkedList()
        circular_linked_list.insertTail(Node(1))
        circular_linked_list.insertTail(Node(2))
        circular_linked_list.insertTail(Node(3))
        assert circular_linked_list.head.value == 1
        assert circular_linked_list.tail.value == 3
        assert circular_linked_list.length == 3
    
    def insert_test():
        # Test the insert() method
        circular_linked_list = CircularLinkedList()
        circular_linked_list.insert(Node(1), 0)
        circular_linked_list.insert(Node(2), 1)
        circular_linked_list.insert(Node(3), 2)
        assert circular_linked_list.head.value == 1
        assert circular_linked_list.tail.value == 3 
        assert circular_linked_list.length == 3

    def deleteHead_test():
        # Test the deleteHead() method
        circular_linked_list = CircularLinkedList()
        circular_linked_list.insertTail(Node(1))
        circular_linked_list.insertTail(Node(2))
        circular_linked_list.insertTail(Node(3))
        circular_linked_list.deleteHead()
        assert circular_linked_list.head.value == 2
        assert circular_linked_list.tail.value == 3
        assert circular_linked_list.length == 2
    
    def deleteTail_test():
        # Test the deleteTail() method
        circular_linked_list = CircularLinkedList()
        circular_linked_list.insertTail(Node(1))
        circular_linked_list.insertTail(Node(2))
        circular_linked_list.insertTail(Node(3))
        circular_linked_list.deleteTail()
        assert circular_linked_list.head.value == 1
        assert circular_linked_list.tail.value == 2
        assert circular_linked_list.length == 2

    def delete_test():
        # Test the delete() method
        circular_linked_list = CircularLinkedList()
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        circular_linked_list.insertTail(node1)
        circular_linked_list.insertTail(node2)
        circular_linked_list.insertTail(node3)
        circular_linked_list.delete(node2)
        assert circular_linked_list.head.value == 1
        assert circular_linked_list.tail.value == 3
        assert circular_linked_list.length == 2

    
    def clear_test():
        # Test the clear() method
        circular_linked_list = CircularLinkedList()
        circular_linked_list.insertTail(Node(1))
        circular_linked_list.insertTail(Node(2))
        circular_linked_list.insertTail(Node(3))
        circular_linked_list.clear()
        assert circular_linked_list.head is None
        assert circular_linked_list.tail is None
        assert circular_linked_list.length == 0

    def sort_test():
        # Test the sort() method
        circular_linked_list = CircularLinkedList()
        circular_linked_list.insertTail(Node(3))
        circular_linked_list.insertTail(Node(1))
        circular_linked_list.insertTail(Node(2))
        circular_linked_list.sort()
        assert circular_linked_list.head.value == 1
        assert circular_linked_list.tail.value == 3
        assert circular_linked_list.length == 3

    def search_test():
        # Test the search() method
        circular_linked_list = CircularLinkedList()
        node2 = Node(2)
        node1 = Node(1)
        node3 = Node(3)
        circular_linked_list.insertTail(node1)
        circular_linked_list.insertTail(node2)
        circular_linked_list.insertTail(node3)
        assert circular_linked_list.search(node2).value == 2
        assert circular_linked_list.search(Node(4)) is None

    search_test()
    insertHead_test()
    insertTail_test()
    insert_test()
    deleteHead_test()
    deleteTail_test()
    delete_test()
    clear_test()
    sort_test()

# DONE
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

# DONE
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

# DONE
def test_BST():
    from mylib.datastructures.trees.BST import BinarySearchTree as BST
    from mylib.datastructures.nodes.Tree_Node import Node
    def insert_test():
        # Test the insert() method
        bst = BST()
        bst.insert(Node(5))
        bst.insert(Node(3))
        bst.insert(Node(7))
        bst.insert(Node(2))
        bst.insert(Node(4))
        bst.insert(Node(6))
        bst.insert(Node(8))
        # bst.printBF()
        assert bst.root.data == 5
        assert bst.root.left.data == 3
        assert bst.root.right.data == 7
        assert bst.root.left.left.data == 2
        assert bst.root.left.right.data == 4
        assert bst.root.right.left.data == 6
        assert bst.root.right.right.data == 8
    
    def search_test():
        # Test the search() method
        bst = BST()
        bst.insert(Node(5))
        bst.insert(Node(3))
        bst.insert(Node(7))
        bst.insert(Node(2))
        bst.insert(Node(4))
        bst.insert(Node(6))
        bst.insert(Node(8))
        assert bst.search(2).data == 2
        assert bst.search(10) is None

    def delete_test():
        # Test the delete() method
        bst = BST()
        bst.insert(Node(5))
        bst.insert(Node(3))
        bst.insert(Node(7))
        bst.insert(Node(2))
        bst.insert(Node(4))
        bst.insert(Node(6))
        bst.insert(Node(8))
        bst.delete(3)
        assert bst.root.left.data == 4
        assert bst.root.left.left.data == 2
        bst.delete(7)
        bst.printBF()
        assert bst.root.right.data == 8
        assert bst.root.right.left.data == 6

    insert_test()
    search_test()
    delete_test()

# DONE
def test_AVL():
    from mylib.datastructures.trees.AVL import AVLTree as AVL
    from mylib.datastructures.nodes.Tree_Node import Node
    def init_test():
        # Test the init() method
        avl = AVL()
        assert avl.root is None

    def init_test_2():
        # Test the init() method
        avl = AVL(Node(5))
        assert avl.root.data == 5

    def insert_test():
        # Test the insert() method
        avl = AVL()
        avl.insert(Node(5))
        avl.insert(Node(3))
        avl.insert(Node(7))
        avl.insert(Node(2))
        avl.insert(Node(4))
        avl.insert(Node(6))
        avl.insert(Node(8))
        assert avl.root.data == 5
        assert avl.root.left.data == 3
        assert avl.root.right.data == 7
        assert avl.root.left.left.data == 2
        assert avl.root.left.right.data == 4
        assert avl.root.right.left.data == 6
        assert avl.root.right.right.data == 8

    def search_test():
        # Test the search() method
        avl = AVL()
        avl.insert(Node(5))
        avl.insert(Node(3))
        avl.insert(Node(7))
        avl.insert(Node(2))
        avl.insert(Node(4))
        avl.insert(Node(8))
        assert avl.search(2).data == 2
        assert avl.search(10) is None

    def delete_test():
        # Test the delete() method
        avl = AVL()
        avl.insert(Node(5))
        avl.insert(Node(3))
        avl.insert(Node(7))
        avl.insert(Node(2))
        avl.insert(Node(4))
        avl.insert(Node(6))
        avl.insert(Node(8))
        avl.delete(3)
        assert avl.root.left.data == 2
        assert avl.root.left.right.data == 4
        avl.delete(7)
        assert avl.root.right.data == 6
        assert avl.root.right.right.data == 8

    init_test()
    init_test_2()
    insert_test()
    search_test()
    delete_test()

#NOT DONE (sortfunction is broken!)
def test_VBH_Max():
    from mylib.datastructures.heap.VBH_Max import MaxHeap as MaxHeap
    
    def init_test():
        # Test the init() method
        max_heap = MaxHeap()
        assert max_heap.getSize() == 0
        assert max_heap.isEmpty() == True

    def insert_test():
        # Test the insert() method
        max_heap = MaxHeap()
        max_heap.insert(10)
        max_heap.insert(20)
        max_heap.insert(15)
        assert max_heap.getSize() == 3
        assert max_heap.isEmpty() == False
        assert max_heap.contains(10) == True

    def delete_test():
        # Test the delete() method
        max_heap = MaxHeap()
        max_heap.insert(10)
        max_heap.insert(20)
        max_heap.insert(15)
        max_heap.delete(10)
        assert max_heap.getSize() == 2
        assert max_heap.isEmpty() == False
        assert max_heap.contains(10) == False

    def clear_test():
        # Test the clear() method
        max_heap = MaxHeap()
        max_heap.insert(10)
        max_heap.insert(20)
        max_heap.insert(15)
        assert max_heap.getSize() == 3
        max_heap.clear()
        assert max_heap.getSize() == 0
        assert max_heap.isEmpty() == True
        assert max_heap.contains(10) == False

    def sort_test():
        # Test the sort() method
        max_heap = MaxHeap()
        max_heap.insert(10)
        max_heap.insert(20)
        max_heap.insert(15)
        max_heap.sort()
        assert max_heap.getSize() == 3
        assert max_heap.isEmpty() == False
        assert max_heap.contains(10) == True
        assert max_heap.elements[0] == 20
        assert max_heap.elements[1] == 10
        assert max_heap.elements[2] == 15

    init_test()
    insert_test()
    delete_test()
    clear_test()
    sort_test()




#NOT DONE (sortfunction is broken!)
def test_VBH_Min():
    from mylib.datastructures.heap.VBH_Min import MinHeap as MinHeap
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


