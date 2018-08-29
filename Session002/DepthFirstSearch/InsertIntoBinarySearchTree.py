# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        self.insert(root, val)
        return root
    
    def insert(self, node, val):
        if node is None:
            return TreeNode(val)
        if node.val>val:
            if node.left is None:
                node.left=TreeNode(val)
                return
            else:
                self.insert(node.left, val)
        else:
            if node.right is None:
                node.right=TreeNode(val)
                return
            else:
                self.insert(node.right, val)

        return
