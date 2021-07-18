# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.res=[]
        self.dfs(root,"")
        return self.res
    def dfs(self, node, cur:str):
        if node is None:
            return
        if len(cur)==0:
            cur=str(node.val)
        else:
            cur="{0}->{1}".format(cur, str(node.val))
        if node.left is None and node.right is None:
            self.res.append(cur)
            return
        self.dfs(node.left, cur)
        self.dfs(node.right, cur)
        return
        
        