# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    https://leetcode.com/problems/flip-equivalent-binary-trees/
    """
    def flipEquiv(self, root1: 'TreeNode', root2: 'TreeNode') -> bool:
        def dfs(node1,node2):
            if not node1 and not node2:
                return True
            if (not node1 and node2) or (node1 and not node2):
                return False
            if node1.val!=node2.val:
                return False
            return dfs(node1.left,node2.left) and dfs(node1.right, node2.right) or\
                dfs(node1.left, node2.right) and dfs(node1.right, node2.left)
        return dfs(root1, root2)
