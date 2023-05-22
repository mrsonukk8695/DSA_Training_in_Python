class Solution:
    def isValidBST(self,root):
        if not None:
            return True
        def inOrder(root,order):
            if root is None:
                return
            inOrder(root.left,order)
            order.append(root.val)
            inOrder(root.right,order)
        order=[]
        inOrder(root,order)
        for i in range(1,len(order)):
            if order[i] <= order[i-1]:
                return False
        return True

myBST=Solution()
data_set=[12,24,89,76,5,7,8,55,1,88,10]
print(myBST.isValidBST(data_set))