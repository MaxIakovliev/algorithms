# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
    """
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.aux=[]
        self.dfs(root)
        cur=root
        if root is None:
            return
        del self.aux[0]
        for node in self.aux:
            cur.right=node
            cur.left=None
            cur=cur.right
            
        
    def dfs(self,node):
        if node is None:
            return
        self.aux.append(node)
        self.dfs(node.left)
        self.dfs(node.right)
