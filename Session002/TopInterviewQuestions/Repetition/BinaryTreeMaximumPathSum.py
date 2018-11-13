# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if node is None:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            curVal=left+right+node.val
            self.maxSoFar=max(self.maxSoFar,curVal)
            return max(left+node.val, right+node.val,0)
        self.maxSoFar=float('-inf')
        dfs(root)
        return self.maxSoFar


