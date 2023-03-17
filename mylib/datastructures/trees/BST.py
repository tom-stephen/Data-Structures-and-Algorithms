from nodes.Tree_Node import Node

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        def _insert(node, key):
            if not node:
                return Node(key)

            if key < node.key:
                node.left = _insert(node.left, key)
            else:
                node.right = _insert(node.right, key)

            node.height = 1 + max(self._height(node.left), self._height(node.right))
            balance = self._get_balance(node)

            if balance > 1 and key < node.left.key:
                return self._rotate_right(node)
            if balance < -1 and key > node.right.key:
                return self._rotate_left(node)
            if balance > 1 and key > node.left.key:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
            if balance < -1 and key < node.right.key:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

            return node

        self.root = _insert(self.root, key)

    def search(self, key):
        curr_node = self.root
        while curr_node:
            if key == curr_node.key:
                return True
            elif key < curr_node.key:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        return False

    def _height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        new_root.height = 1 + max(self._height(new_root.left), self._height(new_root.right))

        return new_root

    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        new_root.height = 1 + max(self._height(new_root.left), self._height(new_root.right))

        return new_root

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result
