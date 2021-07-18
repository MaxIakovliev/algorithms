# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    https://leetcode.com/problems/range-sum-of-bst/
    """
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        def dfs(node, l,r):
            res=0
            if node is None:
                return 0
            if node.val>=l and node.val<=r:
                res+=node.val
            res+=dfs(node.left,l,r)
            res+=dfs(node.right,l,r)
            return res
        return dfs(root,L,R)
        
        
        self.res=0

