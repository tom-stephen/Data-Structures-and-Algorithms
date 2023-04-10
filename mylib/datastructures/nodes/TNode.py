class TNode:
    #two constructors stuffed into one (i am in misery)
    def __init__(self, data = 0, balance = 0, P = None, L = None, R = None): 

        if(data == 0 and balance == 0 and P == None and L == None and R == None):
            self.dataMember = 0
            self.left = None
            self.right = None
            self.parent = None
            self.balance = 0
        else:
            self.dataMember = data
            self.balance = balance
            self.parent = P
            self.left = L
            self.right = R            

    def setDataMember(self, data):
        self.dataMember = data
    def setTNodeLeft(self, L):
        self.left = L
    def setTNodeRight(self, R):
        self.right = R
    def setTNodeParent(self, P):
        self.parent = P
    def setBalance(self, balance):
        self.balance = balance


    def getDataMember(self):
        return self.dataMember
    def getTNodeLeft(self):
        return self.left
    def getTNodeRight(self): 
        return self.right
    def getTNodeParent(self): 
        return self.parent
    def getBalance(self):  
        return self.balance
    
    def print(self):
        print("Data_Member: ", self.dataMember, "\nBalance: ", self.balance)

    def toString(self):
        output = str(self.dataMember)
        return output
