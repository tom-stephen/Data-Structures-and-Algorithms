#from mylib.datastructures.trees.TNode import TNode
from TNode import TNode


class BST:    
    #3 constructors in one (reeses puff)
    def __init__(self, val = 0, obj = None):
        self.root = None
        def construct(val):
            return TNode(val, 0, None, None, None)
        if(val ==0 and obj == None):
            self.root = None
        elif(obj == None):
            self.root = construct(val)
        elif(val ==0):
            self.root = obj


    def setRoot(self, root):        #NEEDS WORK
        self.root = root

    def getRoot(self):
        return self.root
    
    def insert(self, val):         
        newNode = TNode(val, 0, None, None, None)
        if self.root == None:
            self.root = newNode
        else:
            current = self.root
            while(True):
                parent = current
                if(val < current.getDataMember()):
                    current = current.getTNodeLeft()

                    #parent.setBalance(parent.getBalance() - 1)
                    #print("Test Balance P: ", parent.getBalance())

                    if(current == None):
                        current = newNode
                        parent.setTNodeLeft(current)
                        current.setTNodeParent(parent)
                        return
                else:
                    current = current.getTNodeRight()

                    #parent.setBalance(parent.getBalance() + 1)
                    #print("Test Balance P: ", parent.getBalance())

                    if(current == None):
                        current = newNode
                        parent.setTNodeRight(current)
                        current.setTNodeParent(parent)
                        return


    def insertNode(self, node):
        if self.root == None:
            self.root = node
        else:
            current = self.root
            while(True):
                parent = current
                if(node.getDataMember() < current.getDataMember()):
                    current = current.getTNodeLeft()

                    #parent.setBalance(parent.getBalance() - 1)

                    if(current == None):
                        current = node
                        parent.setTNodeLeft(current)
                        current.setTNodeParent(parent)
                        return
                else:
                    current = current.getTNodeRight()

                    #parent.setBalance(parent.getBalance() + 1)

                    if(current == None):
                        current = node
                        parent.setTNodeRight(current)
                        current.setTNodeParent(parent)
                        return                


    def Delete(self, val):      ###very basic implementation, deletes node and the branches below it
        
        parent = self.root
        current = parent
        temp = current
        while(current != None and current.getDataMember() != val):
            if(val < current.getDataMember()):
                parent = current
                current = current.getTNodeLeft()
                temp = current
            else:
                parent = current
                current = current.getTNodeRight()
                temp = current
        if(current == None):
            print("Value Cannot be found")
            return None
        if(parent.getTNodeLeft() == current):
            parent.setTNodeLeft(None)

        else:
            parent.setTNodeLeft(None)

                   
    def Search(self, val):
        current = self.root
        while(current != None and current.getDataMember() != val):
            if(val < current.getDataMember()):
                current = current.getTNodeLeft()
            else:
                current = current.getTNodeRight()
        if(current == None):
            return None
        return current
            



    def printInOrder(self):
        def _inorder_traversal(node, result):
            if (node == None):
                return
            if(node.getTNodeLeft() != None):
                _inorder_traversal(node.getTNodeLeft(), result)
            result.append(node.getDataMember())
            if(node.getTNodeRight() != None):
                _inorder_traversal(node.getTNodeRight(), result)
            return result

        result = []
        _inorder_traversal(self.root, result)

        print("Contents of BST in ascending order: ")
        print(result)



    def printBF(self):
        def _inorder_traversal(node, result, level):
            if (node == None):
                return
            result[node.getDataMember()] = level
            level += 1
            if(node.getTNodeLeft() != None):
                (_inorder_traversal(node.getTNodeLeft(), result, level))
            if(node.getTNodeRight() != None):
                (_inorder_traversal(node.getTNodeRight(), result, level))
            return result

        result = {}
        level = 0
        _inorder_traversal(self.root, result, level)

        sorted_dt = {key: value for key, value in sorted(result.items(), key=lambda item: item[1])}

        print("How to Read: (Value: Depth)")
        print(sorted_dt)

'''
   def printBF(self):
        def _inorder_traversal(node):
            if (node == None):
                print()
            left = node.getTNodeLeft()
            right = node.getTNodeRight()
            if(left != None and right != None):
                print(node.getDataMember(),":",left.getDataMember()," ", right.getDataMember())
            elif(left == None and right != None):
                print(node.getDataMember(),":","null"," ", right.getDataMember())
            elif(left != None and right == None):   
                print(node.getDataMember(),":",left.getDataMember()," ","null")
            else:
                print(node.getDataMember(),":","null"," ", "null")
            

            if(node.getTNodeLeft() != None):
                _inorder_traversal(node.getTNodeLeft())


            if(node.getTNodeRight() != None):
                _inorder_traversal(node.getTNodeRight())

        _inorder_traversal(self.root)
'''


#Testing
if __name__ == "__main__":
    b = TNode(9)
    a = BST(15)
    #print("Root:", a.getRoot())
    a.insertNode(b)
    a.insert(2)
    #a.Search(2)
    a.Delete(2)
    a.Delete(2)
    a.Search(2)
    a.insert(3)
    a.insert(5)

    a.printInOrder()
    a.printBF()
    #print(a.Search(2))