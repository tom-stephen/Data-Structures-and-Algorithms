from mylib.datastructures.nodes.Tree_Node import Node
from mylib.datastructures.trees.BST import BinarySearchTree as BST


class AVLTree(BST):

    def __init__(self, root=None):
        # check if root is a Node
        if root and not isinstance(root, Node):
            self.root = Node(root)
        else:
            self.root = root
            return
        
        # check if the tree is balanced if it is not empty
        lHeight = 0
        rHeight = 0
        if self.root.left:
            lHeight = self._height(self.root.left)
        if self.root.right:
            rHeight = self._height(self.root.right)

        if abs(lHeight - rHeight) > 1:
            self.root = self._rebalance(self.root)
        
    def _rebalance(self, node):
        # check if the tree is balanced if it is not empty
        lHeight = 0
        rHeight = 0
        if node.left:
            lHeight = self._height(node.left)
        if node.right:
            rHeight = self._height(node.right)

        if abs(lHeight - rHeight) > 1:
            if lHeight > rHeight:
                if self._height(node.left.left) >= self._height(node.left.right):
                    node = self._right_rotate(node)
                else:
                    node.left = self._left_rotate(node.left)
                    node = self._right_rotate(node)
            else:
                if self._height(node.right.right) >= self._height(node.right.left):
                    node = self._left_rotate(node)
                else:
                    node.right = self._right_rotate(node.right)
                    node = self._left_rotate(node)
        return node
    
    def _right_rotate(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root
    
    def _left_rotate(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root
    
    def _height(self, node):
        # helper method to compute the height of a node (number of edges in the longest path from the node to a leaf)
        if not node:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))
    
    def insert(self, node):
        super().insert(node)
        self.root = self._rebalance(self.root)

    def delete(self, val):
        super().delete(val)
        self.root = self._rebalance(self.root)
    
    def search(self, data):
        return super().search(data)
    
    def printInOrder(self):
        return super().printInOrder()
    
    def printBF(self):
        return super().printBF()
    
    


          