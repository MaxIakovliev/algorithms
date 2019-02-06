# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxVal=0
        self.search(root,root.val)
        return self.maxVal

    def search(self, node, prevVal):
        if node is None:
            return 0
        left=self.search(node.left, node.val)
        right=self.search(node.right, node.val)
        
        self.maxVal=max(self.maxVal, left+right)
        if node.val==prevVal:
            return max(left,right)+1
        return 0



    def longestUnivaluePath2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, prevVal):
            if node is None:
                return 0
            left=dfs(node.left, node.val)        
            right=dfs(node.right, node.val)        
            self.maxVal=max(self.maxVal, left+right)
            if node.val==prevVal:
                return max(left, right)+1
            return 0
        
        self.maxVal=0
        dfs(root,root.val)
        return self.maxVal

 
        
        


