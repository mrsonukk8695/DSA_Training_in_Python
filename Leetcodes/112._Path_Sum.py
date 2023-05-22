#DFS
class Solution:
    def hasPathSum(self,root,target):
        if not root:
            return False
        if root.left is None and root.right is None and target==root.val:
            return True
        return (self.hasPathSum(root.left,target-root.val)) or self.hasPathSum(root.right,target-root.val)




'''class Solution:
    def hasPathSum(self,root,target):
        if not root:
            return False
        num=0
        num+=root.val
        if root.left is None and root.right is None :
            return target==num
        return self.hasPathSum(root.left,target) or self.hasPathSum(root.right,target)
        '''