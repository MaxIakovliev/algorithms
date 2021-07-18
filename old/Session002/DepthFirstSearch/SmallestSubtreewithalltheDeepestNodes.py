# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if node is None:
                return 0
            return max(dfs(node.left),dfs(node.right))+1
        if root is None:
            return None
        l=dfs(root.left)
        r=dfs(root.right)
        if l==r:
            return root
        elif l>r:
            return self.subtreeWithAllDeepest(root.left)
        else:
            return self.subtreeWithAllDeepest(root.right)

        