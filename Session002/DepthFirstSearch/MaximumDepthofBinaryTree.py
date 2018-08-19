# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root,1)
    def dfs(self, node, depth):
        if node is None:
            return depth-1
        if node.left is None and node.right is None:
            return depth
        
        tmpDepth=depth
        if node.left is not None:
            tmp=self.dfs(node.left, tmpDepth+1)
            depth=max(depth,tmp)
        
        if node.right is not None:
            tmp=self.dfs(node.right, tmpDepth+1)
            depth=max(depth,tmp)
        
        return depth

    