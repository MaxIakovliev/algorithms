# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    https://leetcode.com/problems/recover-binary-search-tree/description/
    """
 
        
        
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.err1=TreeNode(None)
        self.err2=TreeNode(None)
        self.prev=TreeNode(float('-inf'))
        self.traverse(root)

        tmp=self.err1.val
        self.err1.val=self.err2.val
        self.err2.val=tmp


    def traverse(self, node):
        if node is None:
            return

        self.traverse(node.left)

        if self.err1.val==None and self.prev.val>=node.val:
            self.err1=self.prev
        
        if self.err1.val!=None and self.prev.val>=node.val:
            self.err2=node

        self.prev=node

        self.traverse(node.right)


