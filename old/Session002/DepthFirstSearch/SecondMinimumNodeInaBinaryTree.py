# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def bfs(node):
            if node is None:
                return
            
            if root.val< node.val and node.val<self.secondMin:
                self.secondMin=node.val
            bfs(node.left)
            bfs(node.right)
            
        self.secondMin=float('inf')
        bfs(root)
        if self.secondMin==float('inf'):
            return -1
        return self.secondMin