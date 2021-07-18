# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    https://leetcode.com/problems/path-sum/description/
    """
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.dfs(root, 0, sum)

    def dfs(self, node, curSum, reqSum):
        if node is None:
            return False
        elif node.val+curSum==reqSum and node.left is None and node.right is None:
            return True
        else:
            return self.dfs(node.left, curSum+node.val, reqSum) or self.dfs(node.right, curSum+node.val, reqSum)
        

         
        