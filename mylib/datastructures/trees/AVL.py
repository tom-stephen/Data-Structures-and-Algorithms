from nodes.TNode import TNode
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
        def _pivotUpdateCheck(root, val, ancestor, pivot, son):
            current = root
            while(current != None and current.getDataMember() != val):
                if(val < current.getDataMember()):
                    current = current.getTNodeLeft()
                else:
                    current = current.getTNodeRight()
            if(ancestor != None):
                if(son.getTNodeRight() == current.getTNodeParent() and pivot.getBalance() == 1 and (ancestor.getBalance() == -1 or ancestor.getBalance() == 1)):
                    return "leftRotate"
                elif(son.getTNodeLeft() == current.getTNodeParent() and pivot.getBalance() == 1 and (ancestor.getBalance() == -1 or ancestor.getBalance() == 1)):
                    return "rlRotate"
                elif(son.getTNodeLeft() == current.getTNodeParent() and pivot.getBalance() == -1 and (ancestor.getBalance() == -1 or ancestor.getBalance() == 1)):
                    return "rightRotate"
                elif(son.getTNodeRight() == current.getTNodeParent() and pivot.getBalance() == -1 and (ancestor.getBalance() == -1 or ancestor.getBalance() == 1)):
                    return "lrRotate"
                else:
                    return "skip"
            else:
                if((son.getTNodeRight() == current or son.getTNodeRight() == current.getTNodeParent()) and pivot.getBalance() == 1):
                    return "leftRotate"
                elif((son.getTNodeLeft() == current or son.getTNodeLeft() == current.getTNodeParent()) and pivot.getBalance() == 1):
                    return "rlRotate"
                elif((son.getTNodeLeft() == current or son.getTNodeLeft() == current.getTNodeParent()) and pivot.getBalance() == -1):
                    return "rightRotate"
                elif((son.getTNodeRight() == current or son.getTNodeRight() == current.getTNodeParent()) and pivot.getBalance() == -1):
                    return "lrRotate"
                else:
                    return "skip"
                    

        def rightRotate(root, ancestor, pivot, son):
            if(ancestor == None):
                pivot.setTNodeLeft(None)
                pivot.setTNodeParent(None)

                son.setTNodeParent(ancestor)

                if(son.getTNodeRight() != None):
                    temp = son.getTNodeRight()
                    pivot.setTNodeLeft(temp)
                    temp.setTNodeParent(pivot)
                    son.setTNodeRight(None)

                son.setTNodeRight(pivot)
                pivot.setTNodeParent(son)
            else:
                pivot.setTNodeLeft(None)
                pivot.setTNodeParent(None)

                if(son.getTNodeRight() != None):
                    temp = son.getTNodeRight()
                    pivot.setTNodeLeft(temp)
                    temp.setTNodeParent(pivot)
                    son.setTNodeRight(None)

                if(ancestor.getTNodeLeft() == pivot):
                    ancestor.setTNodeLeft(son)
                else:
                    ancestor.setTNodeRight(son)

                son.setTNodeParent(ancestor)

                son.setTNodeRight(pivot)
                pivot.setTNodeParent(son)
             
        def leftRotate(root, ancestor, pivot, son):
            if(ancestor == None):
                pivot.setTNodeRight(None)
                pivot.setTNodeParent(None)

                son.setTNodeParent(ancestor)

                if(son.getTNodeLeft() != None):
                    temp = son.getTNodeLeft()
                    pivot.setTNodeRight(temp)
                    temp.setTNodeParent(pivot)
                    son.setTNodeLeft(None)

                son.setTNodeLeft(pivot)
                pivot.setTNodeParent(son)
            else:
                pivot.setTNodeRight(None)
                pivot.setTNodeParent(None)

                if(son.getTNodeLeft() != None):
                    temp = son.getTNodeLeft()
                    pivot.setTNodeRight(temp)
                    temp.setTNodeParent(pivot)
                    son.setTNodeLeft(None)

                if(ancestor.getTNodeLeft() == pivot):
                    ancestor.setTNodeLeft(son)
                else:
                    ancestor.setTNodeRight(son)

                son.setTNodeParent(ancestor)

                son.setTNodeLeft(pivot)
                pivot.setTNodeParent(son)                 


        ancestor = None
        pivot = None
        son = None
        super().insert(val)
        pivot = _pivotFind(self.root, val)
        son = _pivotSonFind(self.root, val)

        #CHECKS IF THERE NEEDS TO BE A PIVOT CHANGE

        #_balanceUpdate(self.root)

        #print(self.root.getBalance())
        if(pivot != None):                           
            ancestor = pivot.getTNodeParent()

            check = _pivotUpdateCheck(self.root, val, ancestor, pivot, son)


            #print(check)

            if(check != "skip"):
                if(check == "leftRotate"):
                    leftRotate(self.root, ancestor, pivot, son)
                    if(ancestor == None):
                        super().setRoot(son)
                elif(check == "rightRotate"):
                    rightRotate(self.root, ancestor, pivot, son)
                    if(ancestor == None):
                        super().setRoot(son)
                elif(check == "rlRotate"):
                    grandson = son.getTNodeLeft()
                    #rlRotate(self.root, ancestor, pivot, son, grandson)

                    rightRotate(self.root, pivot, son, grandson)
                    leftRotate(self.root, ancestor, pivot, grandson)
                    if(ancestor == None):
                        super().setRoot(grandson)
                elif(check == "lrRotate"):
                    grandson = son.getTNodeRight()
                    #lrRotate(self.root, ancestor, pivot, son, grandson)

                    leftRotate(self.root, pivot, son, grandson)
                    rightRotate(self.root, ancestor, pivot, grandson)
                    if(ancestor == None):
                        super().setRoot(grandson)
           
                    

        _balanceUpdate(self.root)


        #print("root balance:", super().getRoot().getBalance())

    def insertNode(self, node):
        super().insert(node)



    def Search(self, val):
        super().Search(val)

    def printInOder(self):
        super().printInOrder
    def printBF(self):
        super().printBF()

if __name__ == "__main__":

    a = AVL(60)

    b = TNode(80)

    a.insert(b)
    a.insert(40)
    a.insert(95)
    a.insert(70)
    a.insert(75)
    '''
    print()
    a = AVL(60)
    a.insert(50)
    a.insert(70)
    a.insert(40)
    a.insert(65)
    a.insert(80)
    a.insert(75)
    a.insert(90)
    a.insert(85)
    '''
    '''
    a = AVL(8)
    a.insert(5)
    a.insert(3)
    a.insert(7)
    a.insert(2)
    a.insert(4)
    a.insert(6)
    '''
    '''
    a.insert(80)
    a.insert(40)
    a.insert(95)
    a.insert(20)
    a.insert(30)
    a.insert(50)
    a.insert(10)
    a.insert(5)
    '''

    #a.printInOrder()
    a.printBF()