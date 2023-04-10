from mylib.datastructures.nodes.Tree_Node import Node

class BinarySearchTree:
    def __init__(self, root=None):
        # check if root is a Node
        if root and not isinstance(root, Node):
            self.root = Node(root)
        else:
            self.root = root

    def insert(self, node):
        # check if node is a Node
        if not isinstance(node, Node):
            node = Node(node)

        # if tree is empty, make node the root
        if not self.root:
            self.root = node
            return

        # traverse the tree to find the appropriate location to insert the new node
        curr_node = self.root
        while curr_node:
            if node.data < curr_node.data:
                if not curr_node.left:
                    curr_node.left = node
                    node.parent = curr_node
                    break
                else:
                    curr_node = curr_node.left
            else:
                if not curr_node.right:
                    curr_node.right = node
                    node.parent = curr_node
                    break
                else:
                    curr_node = curr_node.right
        # update the balance factors of all nodes on the path from the root to the newly inserted node
        self._update_balance(node)

    def _update_balance(self, node):
        # traverse up the tree from the newly inserted node to the root, updating balance factors as necessary
        while node:
            node.balance = self._height(node.right) - self._height(node.left)
            node = node.parent

    def _height(self, node):
        # helper method to compute the height of a node (number of edges in the longest path from the node to a leaf)
        if not node:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))
    

    def search(self, data):
        # traverse the tree to find the node
        curr_node = self.root
        while curr_node:
            if data == curr_node.data:
                return curr_node
            elif data < curr_node.data:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        return None

    def delete(self, value):
        # find the node with the given value in the tree
        node = self.search(value)
        if not node:
            print("Node not found in the tree.")
            return None

        # case 1: node has no children
        if not node.left and not node.right:
            #if the node is not root
            if node.parent:
                if node == node.parent.left:
                    node.parent.left = None
                else:
                    node.parent.right = None
            # if the node is root
            else:
                self.root = None

        # case 2: node has one child
        elif not node.left:
            if node.parent:
                if node == node.parent.left:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right
                node.right.parent = node.parent
            else:
                self.root = node.right
                node.right.parent = None
        elif not node.right:
            if node.parent:
                if node == node.parent.left:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left
                node.left.parent = node.parent
            else:
                self.root = node.left
                node.left.parent = None

        # case 3: node has two children
        else:
            # find the node's successor (the smallest node in the node's right subtree)
            successor = node.right
            while successor.left:
                successor = successor.left

            # replace the node with its successor
            node.data = successor.data
            if successor == node.right:
                node.right = successor.right
                if node.right:
                    node.right.parent = node
            else:
                successor.parent.left = successor.right
                if successor.right:
                    successor.right.parent = successor.parent

        # update balance factors
        if node.parent:
            self._update_balance(node.parent)
        else:
            self._update_balance(self.root)

        return node
    
    def printInOrder(self):
        print("Printing the tree in order:")
        if self.root:
            self.printInOrderHelper(self.root)

    def printInOrderHelper(self, node):
        if node.left:
            self.printInOrderHelper(node.left)
        print(node.data)
        if node.right:
            self.printInOrderHelper(node.right)

    def printBF(self):
        if self.root is None:
            return

        current_level = [self.root]

        while current_level:
            next_level = []
            for node in current_level:
                print(node.data, end=' ')
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            current_level = next_level
            print()



    # def search(self, key):
    #     curr_node = self.root
    #     while curr_node:
    #         if key == curr_node.key:
    #             return True
    #         elif key < curr_node.key:
    #             curr_node = curr_node.left
    #         else:
    #             curr_node = curr_node.right
    #     return False

    # def _height(self, node):
    #     if not node:
    #         return 0
    #     return node.height

    # def _get_balance(self, node):
    #     if not node:
    #         return 0
    #     return self._height(node.left) - self._height(node.right)

    # def _rotate_left(self, node):
    #     new_root = node.right
    #     node.right = new_root.left
    #     new_root.left = node

    #     node.height = 1 + max(self._height(node.left), self._height(node.right))
    #     new_root.height = 1 + max(self._height(new_root.left), self._height(new_root.right))

    #     return new_root

    # def _rotate_right(self, node):
    #     new_root = node.left
    #     node.left = new_root.right
    #     new_root.right = node

    #     node.height = 1 + max(self._height(node.left), self._height(node.right))
    #     new_root.height = 1 + max(self._height(new_root.left), self._height(new_root.right))

    #     return new_root

    # def _inorder_traversal(self, node, result):
    #     if node:
    #         self._inorder_traversal(node.left, result)
    #         result.append(node.key)
    #         self._inorder_traversal(node.right, result)

    # def inorder_traversal(self):
    #     result = []
    #     self._inorder_traversal(self.root, result)
    #     return result
