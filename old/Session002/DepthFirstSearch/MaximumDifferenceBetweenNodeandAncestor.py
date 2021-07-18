# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
    """
    def maxAncestorDiff(self, root: 'TreeNode') -> int:
        def dfs(node, min_val,max_val):
            if not node:
                return
            self.res=max(self.res, abs(node.val-min_val), abs(max_val-node.val))
            min_val=min_val if min_val<node.val else node.val
            max_val=max_val if max_val>node.val else node.val
            dfs(node.left,min_val,max_val)
            dfs(node.right,min_val,max_val)
        self.res=0
        dfs(root, root.val,root.val)
        return self.res



                

      