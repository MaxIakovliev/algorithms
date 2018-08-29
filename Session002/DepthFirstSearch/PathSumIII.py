# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    https://leetcode.com/problems/path-sum-iii/description/
    """
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.count=0
        self.countAll(root,0, sum)
        if self.count %2>0:
            return self.count//2-1
        return self.count//2


    def countAll(self, node, cur, sum):
        if node is None:
            return
        
        cur+=node.val
        if cur==sum:
            self.count+=1
        if node.val==sum:
            self.count+=1
        self.countAll(node.left, cur,sum)
        self.countAll(node.left, node.val,sum)
        
        self.countAll(node.right, cur,sum)
        self.countAll(node.right, node.val,sum)
        return
         
        