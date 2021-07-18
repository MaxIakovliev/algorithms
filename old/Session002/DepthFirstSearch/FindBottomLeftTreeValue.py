# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxLevel=0
        self.res=0
        def dfs(node,level):
            if node is None:
                return
            dfs(node.left,level+1)
            dfs(node.right,level+1)

            if level>self.maxLevel:
                self.maxLevel=level
                self.res=node.val
        
        if root is None:
            return None
        dfs(root,1)
        return self.res 

        
    