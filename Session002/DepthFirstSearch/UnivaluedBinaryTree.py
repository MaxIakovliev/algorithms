# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    https://leetcode.com/problems/univalued-binary-tree/
    """
    def isUnivalTree(self, root: TreeNode) -> bool:
        def dfs(node, prev_val):
            if node is None:
                return True
            if node.val!=prev_val:
                return False
            return dfs(node.left,prev_val) and dfs(node.right,prev_val)
        
        return dfs(root,root.val)
        