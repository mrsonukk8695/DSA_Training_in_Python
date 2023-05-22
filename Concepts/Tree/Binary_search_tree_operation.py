class MyNode:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None   
    def MyInsertion(self,data):
        if not self.data:
            self.data=data
            return
        if self.data==data:
            return
        if data<self.data:
            if self.left:
                self.left.MyInsertion(data)
                return
            self.left=MyNode(data)
            return
        if self.right:
            self.right.MyInsertion(data)
            return
        self.right=MyNode(data)
        
    def BST_Search(self, data):
        if self.data==data:
            return True
        if data<self.data:
            if self.left==None:
                return False
            return self.left.BST_Search(data)
        if self.right==None:
            return False
        return self.right.BST_Search(data)
    
    def Preorder(self,values):
        if self.data is not None:
            values.append(self.data)
        if self.left is not None:
            self.left.Preorder(values)
        if self.right is not None:
            self.right.Preorder(values)
        return values
    def InOrder(self,values):
        if self.left is not None:
            self.left.InOrder(values)
        if self.data is not None:
            values.append(self.data)
        if self.right is not None:
            self.right.InOrder(values)
        return values
    def PostOrder(self,values):
        if self.left is not None:
            self.left.PostOrder(values)
        if self.right is not None:
            self.right.PostOrder(values)
        if self.data is not None:
            values.append(self.data)
        return values
    
    
    def getMin(self):
        current=self
        while current.left is not None:
            current=current.left
        return current.data
    
    def getMax(self):
        current=self
        while current.right is not None:
            current=current.right
        return current.data
        
            

treeObj=MyNode()
data_set=[12,24,89,76,5,7,8,55,1,88,10]

for i in data_set:
    treeObj.MyInsertion(i)
print(treeObj.BST_Search(88))

#INORDER 
print("Current Nodes are:",data_set)
print("PreOrder Function:",treeObj.Preorder([]))
print("InOrder Function:",treeObj.InOrder([]))
print("PostOrder Function:",treeObj.PostOrder([]))
print("searching {} in tree {}".format(88,treeObj.BST_Search(88)))
print("The Maximum no {} and Minimum no {} is the tree".format(treeObj.getMax(),treeObj.getMin()))
