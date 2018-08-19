# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    deps=[]
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check(root)!=-1

    def check(self, node):
        if node is None:
            return 0

        left=self.check(node.left)
        right=self.check(node.right)

        if left==-1 or right==-1 or abs(left-right)>1:
            return -1
        return 1+abs(left+right)
        
        
        
    
        
        
