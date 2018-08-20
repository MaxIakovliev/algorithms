# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res=list()
        self.dfs(root,1)
        return self.res

    
    def dfs(self, node, depth):
        if node is None:
            return
        if len(self.res)<depth:
            self.res.append(float("-inf"))
        self.res[depth-1]=max(self.res[depth-1], node.val)
        if node.left is None and node.right is None:
            return
        self.dfs(node.left, depth+1)
        self.dfs(node.right, depth+1)
        return 
        
        