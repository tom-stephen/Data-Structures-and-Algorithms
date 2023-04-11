from mylib.datastructures.linear.SLL import SinglyLinkedList as SLL
from mylib.datastructures.linear.DLL import DoublyLinkedList as DLL
from mylib.datastructures.linear.CDLL import CircularDoublyLinkedList as CDLL
from mylib.datastructures.linear.CSLL import CircularLinkedList as CSLL
from mylib.datastructures.nodes.Single_linked_Node import Node as SNode
from mylib.datastructures.nodes.Doubly_linked_Node import Node as DNode

def test_SLL():
    sll = SLL()

    items = [15, 7, 8, 11, 6, 5, 9, 3, 2, 30]
    # insert elements into the list
    for i in range(10):
        node = SNode(items[i])
        sll.insert(node, i)
    
    sll.print()
    print(sll.head.value)
    print(sll.tail.value)
    sll.sort()
    sll.print()
    print(sll.head.value)
    print("tail is: ",sll.tail)

def test_DLL():
    dll = DLL()

    items = [15, 7, 8, 11, 6, 5, 9, 3, 2, 30]
    # insert elements into the list
    for i in range(10):
        node = DNode(items[i])
        dll.insert(node, i)
    
    dll.print()
    print(dll.head.value)
    print(dll.tail.value)
    dll.sort()
    dll.print()
    print(dll.head.value)
    print("tail is: ",dll.tail)

def test_CDLL():
    cdll = CDLL()

    items = [15, 7, 8, 11, 6, 5, 9, 3, 2, 30]
    # insert elements into the list
    for i in range(10):
        node = DNode(items[i])
        cdll.insert(node, i)
    
    cdll.print()
    print(cdll.head.value)
    print(cdll.tail.value)
    cdll.sort()
    cdll.print()
    print(cdll.head.value)
    print(cdll.tail.value)
    print(cdll.tail.next.value)    
    print(cdll.head.prev.value)    

def test_CSLL():
    csll = CSLL()

    items = [15, 7, 8, 11, 6, 5, 9, 3, 2, 30]
    # insert elements into the list
    for i in range(10):
        node = SNode(items[i])
        csll.insert(node, i)
    
    csll.print()
    print(csll.head.value)
    print(csll.tail.value)
    csll.sort()
    csll.print()
    print(csll.head.value)
    print(csll.tail.value)
    print(csll.tail.next.value)   

def test_BST():
    from mylib.datastructures.trees.BST import BinarySearchTree as BST
    from mylib.datastructures.nodes.Tree_Node import Node
    # Create a new empty BST
    bst = BST()

    # Test insert method
    print("testing the insert method")
    bst.insert(8)
    bst.printBF()
    print()
    bst.insert(5)
    bst.printBF()
    print()
    bst.insert(3)
    bst.printBF()
    print()
    bst.insert(7)
    bst.printBF()
    print()
    bst.insert(2)
    bst.printBF()
    print()
    bst.insert(4)
    bst.printBF()
    print()
    bst.insert(6)
    bst.printBF()
    print()

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

    bst.printInOrder()

def test_AVL():
    from mylib.datastructures.trees.AVL import AVLTree as AVL
    from mylib.datastructures.nodes.Tree_Node import Node
    # Create a new empty BST
    avl = AVL()

    # Test insert method
    print("testing the insert method")
    avl.insert(8)
    avl.printBF()
    print()

    avl.insert(5)
    avl.printBF()
    print()

    avl.insert(3)
    avl.printBF()
    print()

    avl.insert(7)
    avl.printBF()
    print()

    avl.insert(2)
    avl.printBF()
    print()

    avl.insert(4)
    avl.printBF()
    print()

    avl.insert(6)
    avl.printBF()
    print()

    # Test search method
    assert avl.search(5).data == 5
    assert avl.search(3).data == 3
    assert avl.search(7).data == 7
    assert avl.search(2).data == 2
    assert avl.search(4).data == 4
    assert avl.search(6).data == 6
    assert avl.search(8).data == 8
    assert avl.search(1) is None

    print("original tree:")
    avl.printBF()
    print()

    # Test delete method
    avl.delete(5)
    assert avl.search(5) is None
    print("after deleting 5:")
    avl.printBF()
    print()

    avl.delete(3)
    assert avl.search(3) is None
    print("after deleting 3:")
    avl.printBF()
    print()
    ########################## error starts here. it should go into the delte method in BST and then falls under case 1 and the first if
    avl.delete(7)
    assert avl.search(7) is None
    print("after deleting 7:")
    print("avl root: ", avl.root)
    print("avl root right node: ", avl.root.right)
    print("avl root left node: ", avl.root.left)
    print("avl root.left.left: ", avl.root.left.left)
    avl.printBF()
    print()

    avl.delete(2)
    assert avl.search(2) is None
    print("after deleting 2:")
    avl.printBF()
    print()

    avl.delete(4)
    assert avl.search(4) is None
    print("after deleting 4:")
    avl.printBF()
    print()

    avl.delete(6)
    assert avl.search(6) is None
    print("after deleting 6:")
    avl.printBF()
    print()

    avl.delete(8)
    assert avl.search(8) is None
    print("after deleting 8:")
    avl.printBF()
    print()

    # Test print method
    avl.insert(Node(5))
    avl.insert(Node(3))
    avl.insert(Node(7))
    avl.insert(Node(2))
    avl.insert(Node(4))
    avl.insert(Node(6))
    avl.insert(Node(8))
    avl.printBF()

    avl.printInOrder()

test_AVL()