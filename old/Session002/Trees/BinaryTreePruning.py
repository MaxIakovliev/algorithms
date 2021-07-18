# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if node is None:
                return True
            l_res=dfs(node.left)
            r_res=dfs(node.right)
            if l_res:
                node.left=None
            if r_res:
                node.right=None
            if l_res and r_res and node.val==0:
                return True
            return False

        dfs(root)
        return root
        