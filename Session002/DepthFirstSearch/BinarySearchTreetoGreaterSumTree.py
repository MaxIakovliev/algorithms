# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
    solution:
    https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/discuss/286725/JavaC%2B%2BPython-Revered-Inorder-Traversal
    """

    def __init__(self):
        self.prev=0

    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root.right is not None:
            self.bstToGst(root.right)
        root.val=root.val+self.prev
        self.prev=root.val
        if root.left is not None:
            self.bstToGst(root.left)
        return root