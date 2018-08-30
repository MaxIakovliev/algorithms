# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.sumUp(root,0)
    
    def sumUp(self, node, curSum)->(int):
        if node.left is None and node.right is None:
            return curSum*10+node.val
        
        res=0
        if node.left is not None:
            res+=self.sumUp(node.left, curSum*10+node.val)
        if node.right is not None:
            res+=self.sumUp(node.right, curSum*10+node.val)
        return res


