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
        ###DO NOT CHANGE ANYTHING I SPENT 4 HOURS TO GET THIS TO WORK PROPERLY FOR ALL SCENARIOS###
        def _balanceUpdate(node):
            
            node.setBalance(0)
            currentBalance = 0
            childBalance = 0
            levelL = 0
            levelR = 0

            if (node == None):
                return(0)

                #print(levelR)
                #node.setBalance(currentBalance)
                #return(currentBalance)
            if(node.getTNodeLeft() != None):
                childBalance -= abs(_balanceUpdate(node.getTNodeLeft()))
                currentBalance -= 1
            if(node.getTNodeRight() != None):
                childBalance += abs(_balanceUpdate(node.getTNodeRight()))
                currentBalance += 1

            currentBalance += childBalance


            node.setBalance(currentBalance)

            if(node.getTNodeRight() != None and node.getTNodeLeft() != None):
                levelL = 1
                levelR = 1
                levelL += abs(_balanceUpdate(node.getTNodeRight()))
                levelR += abs(_balanceUpdate(node.getTNodeLeft()))

                if(levelR > levelL):
                    return(levelR)
                else:
                    return(levelL)
            #print(node.getBalance())

            return(currentBalance)

        #pivot finders
        def _pivotFind(root, val):
            current = root
            while(current != None and current.getDataMember() != val):
                if(val < current.getDataMember()):
                    current = current.getTNodeLeft()
                else:
                    current = current.getTNodeRight()
            while(current != None and current != root):
                    prev = current
                    current = current.getTNodeParent()
                    if(current.getBalance() != 0):
                        return current
        def _pivotSonFind(root, val):
            current = root
            while(current != None and current.getDataMember() != val):
                if(val < current.getDataMember()):
                    current = current.getTNodeLeft()
                else:
                    current = current.getTNodeRight()
            while(current != None and current != root):
                    prev = current
                    current = current.getTNodeParent()
                    if(current.getBalance() != 0):
                        return prev
        #AVL sorter            
        def _pivotUpdate(root, ancestor, pivot, son):
            if(ancestor == None):
                if(pivot.getBalance() < 0):
                    pivot.setTnodeLeft(None)
                    pivot.setTNodeParent(None)
                    son.setTNodeParent(ancestor)
                    son.setTnodeRight(pivot)
                    pivot.setTNodeParent(son)
                elif(pivot.getBalance() > 0):
                    pivot.setTnodeRight(None)
                    pivot.setTNodeParent(None)
                    son.setTNodeParent(ancestor)
                    son.setTnodeLeft(pivot)
                    pivot.setTNodeParent(son)

                    


        ancestor = None
        pivot = None
        son = None
        super().insert(val)
        pivot = _pivotFind(self.root, val)
        son = _pivotSonFind(self.root, val)

        #CHECKS IF THERE NEEDS TO BE A PIVOT CHANGE
        if(pivot != None):                              #Note to self, expand this for the avl shifts
            ancestor = pivot.getTNodeParent()
            if(ancestor == None):
                super().setRoot(son)
                _pivotUpdate(self.root, ancestor, pivot, son)
            else:
                _pivotUpdate(self.root, ancestor, pivot, son)

        _balanceUpdate(self.root)


        #print("root balance:", super().getRoot().getBalance())

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
    a.insert(80)
    '''
    a.insert(70)
    a.insert(65)
    a.insert(68)

    a.insert(75)
    a.insert(78)
    '''

    #a.printInOrder()
    a.printBF()