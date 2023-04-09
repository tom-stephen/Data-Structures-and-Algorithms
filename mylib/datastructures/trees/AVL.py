from mylib.datastructures.trees.TNode import TNode
#from TNode import TNode

from BST import BST

class AVL(BST):


    def __init__(self, val = 0, obj = None):
        self.root = None
        if(val ==0 and obj == None):
            super().__init__()
        elif(obj == None):
            super().__init__(val)
        elif(val ==0):
            super().__init__(obj)
        
    def insert(self, val):
        super().insert(val)
        #print("root balance: ", super().getRoot().getBalance())
        
        

    def insertNode(self, node):
        super().insert(node)


    def Search(self):
        super().Search()

    def printInOder(self):
        super().printInOrder
    def printBF(self):
        super().printBF()

if __name__ == "__main__":
    print()
    a = AVL(60)
    a.insert(70)
    a.insert(40)
    a.insert(30)
    a.insert(8)
    a.printInOrder()
    a.printBF()
