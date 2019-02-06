# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    https://leetcode.com/problems/binary-tree-cameras/description/
    """
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result=0
        def dfs(node):
            if not node:
                return 2
            left=dfs(node.left)
            right=dfs(node.right)
            if left==0 or right==0:
                self.result+=1
                return 1
            return 2 if left==1 or right==1 else 0
        return (dfs(root)==0)+self.result

        