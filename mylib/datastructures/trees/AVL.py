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
        def _pivotUpdateCheck(root, val, pivot, son):
            current = root
            while(current != None and current.getDataMember() != val):
                if(val < current.getDataMember()):
                    current = current.getTNodeLeft()
                else:
                    current = current.getTNodeRight()
            if(son.getTNodeRight() == current and pivot.getBalance() == 1):
                return "leftRotate"
            if(son.getTNodeLeft() == current and pivot.getBalance() == 1):
                return "rlRotate"
            if(son.getTNodeLeft() == current or son.getTNodeRight() == -1):
                return "rightRotate"
            if(son.getTNodeRight() == current or son.getTNodeRight() == -1):
                return "lrRotate"
            else:
                return "skip"
                    

        def rightRotate(root, ancestor, pivot, son):
            if(ancestor == None):
                pivot.setTNodeLeft(None)
                pivot.setTNodeParent(None)

                son.setTNodeParent(ancestor)
                son.setTNodeRight(pivot)
                pivot.setTNodeParent(son)
            else:
                pivot.setTNodeLeft(None)
                pivot.setTNodeParent(None)

                ancestor.setTNodeRight(son)
                son.setTNodeParent(ancestor)

                son.setTNodeRight(pivot)
                pivot.setTNodeParent(son)
             
        def leftRotate(root, ancestor, pivot, son):
            if(ancestor == None):
                pivot.setTNodeRight(None)
                pivot.setTNodeParent(None)

                son.setTNodeParent(ancestor)

                son.setTNodeLeft(pivot)
                pivot.setTNodeParent(son)
            else:
                pivot.setTNodeRight(None)
                pivot.setTNodeParent(None)

                ancestor.setTNodeLeft(son)
                son.setTNodeParent(ancestor)

                son.setTNodeLeft(pivot)
                pivot.setTNodeParent(son)   

                    


        ancestor = None
        ancestor = None
        pivot = None
        son = None
        super().insert(val)
        pivot = _pivotFind(self.root, val)
        son = _pivotSonFind(self.root, val)

        #CHECKS IF THERE NEEDS TO BE A PIVOT CHANGE
        if(pivot != None):                           
            ancestor = pivot.getTNodeParent()

            check = _pivotUpdateCheck(self.root, val, pivot, son)

            if(check != "skip"):
                if(check == "leftRotate"):
                    leftRotate(self.root, ancestor, pivot, son)
                    super().setRoot(son)
                elif(check == "rightRotate"):
                    rightRotate(self.root, ancestor, pivot, son)
                    super().setRoot(son)
                elif(check == "rlRotate"):
                    grandson = son.getTNodeLeft()
                    rightRotate(self.root, pivot, son, grandson)
                    leftRotate(self.root, ancestor, pivot, grandson)
                    super().setRoot(grandson)
                elif(check == "lrRotate"):
                    grandson = son.getTNodeRight()
                    leftRotate(self.root, pivot, son, grandson)
                    rightRotate(self.root, ancestor, pivot, grandson)
                    super().setRoot(grandson)
           
                    

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
    #a.insert(70)
    a.insert(70)
    a.insert(65)
    #a.insert(80)
    '''
    a.insert(70)
    a.insert(65)
    a.insert(68)

    a.insert(75)
    a.insert(78)
    '''

    #a.printInOrder()
    a.printBF()