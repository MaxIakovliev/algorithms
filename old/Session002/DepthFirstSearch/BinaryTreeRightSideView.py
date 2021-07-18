# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    https://leetcode.com/problems/binary-tree-right-side-view/description/
    """
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(node,level):
            if node is None:
                return
            if level<len(self.data):
                self.data[level]=node.val
            else:
                self.data.append(node.val)
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        self.data=[]
        dfs(root,0)
        return self.data
   