# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    https://leetcode.com/problems/search-in-a-binary-search-tree/description/
    """
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        return self.search(root,val)
    
    def search(self,node, val):
        if node is None:
            return None
        
        if node.val==val:
            return node
        elif node.val>val:
            return self.search(node.left, val)
        else:
            return self.search(node.right, val)
        