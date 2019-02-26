# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(a,b)->bool:
            if a is None and b is None:
                return True
            if a is None or b is None or a.val!=b.val:
                return False
            else:
                return (
                    dfs(a.left, b.left) and dfs(a.right, b.right)
                 or
                    dfs(a.left, b.right) and dfs(a.right, b.left)
                        )
        
        return dfs(root1,root2)
