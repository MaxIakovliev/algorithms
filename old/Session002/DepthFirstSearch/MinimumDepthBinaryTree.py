# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
    """
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root)
    def dfs(self,node):
        if node is None:
            return 0
        left=self.dfs(node.left)
        right=self.dfs(node.right)
        if right>0 and left>0:
            return 1+(min(left,right))
        return 1+max(left,right)
     