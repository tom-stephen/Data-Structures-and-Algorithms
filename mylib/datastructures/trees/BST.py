from mylib.datastructures.trees.TNode import TNode
#from TNode import TNode


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
    
    def insert(self, val):          ###I HAVE NOT IMPLEMENTED THE BALANCE OR PARENT
        newNode = TNode(val, 0, None, None, None)
        if self.root == None:
            self.root = newNode
        else:
            current = self.root
            while(True):
                parent = current
                if(val < current.getDataMember()):
                    current = current.getTNodeLeft()
                    if(current == None):
                        current = newNode
                        parent.setTnodeLeft(current)
                        current.setTNodeParent(parent)

                        print("LEFT B")
                        print("NodeNum P:", parent.toString())
                        print("NodeNum C:", current.toString())
                        print("Test Left P: ", parent.getTNodeLeft())
                        print("Test Right P: ", parent.getTNodeRight())
                        print("Test Balance P: ", parent.getBalance())
                        print("Test Left C: ", current.getTNodeLeft())
                        print("Test Left C: ", current.getTNodeRight())
                        print("Test Left C-P: ", current.getTNodeParent())

                        return
                else:
                    current = current.getTNodeRight()
                    if(current == None):
                        current = newNode
                        parent.setTnodeRight(current)
                        current.setTNodeParent(parent)

                        print("RIGHT B")
                        print("NodeNum P:", parent.toString())
                        print("NodeNum C:", current.toString())
                        print("Test Left P: ", parent.getTNodeLeft())
                        print("Test Right P: ", parent.getTNodeRight())
                        print("Test Balance P: ", parent.getBalance())
                        print("Test Left C: ", current.getTNodeLeft())
                        print("Test Left C: ", current.getTNodeRight())
                        print("Test Left C-P: ", current.getTNodeParent())
                        return

'''
    def insert(self, TNode):



    def Delete(val):

    def Search(TNode):

    def printInOrder(self):

    def printBF():
'''

if __name__ == "__main__":
    a = BST(8)
    print("Root:", a.getRoot())
    a.insert(10)
    a.insert(4)
    a.insert(2)
    a.insert(9)
    print("Root:", a.getRoot())