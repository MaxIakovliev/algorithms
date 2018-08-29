# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
    """
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxSoFar=float('-inf')
        self.dfs(root)
        return self.maxSoFar

    def dfs(self, node):
        if node is None:
            return 0
        left=self.dfs(node.left)
        right=self.dfs(node.right)
        curSum=left+right+node.val
        self.maxSoFar=max(self.maxSoFar, curSum)

        return max(left+node.val, right+node.val,0)
        