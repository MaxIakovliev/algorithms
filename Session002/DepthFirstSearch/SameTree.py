# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        self.st1=list()
        self.st2=list()
        self.dfs(p,self.st1)
        self.dfs(q,self.st2)
        if len(self.st1)!=len(self.st2):
            return False
        for i in range(len(self.st1)):
            if self.st1[i]!=self.st2[i]:
                return False
        return True


    def dfs(self, node, stack:list)->(None):
        if node is None:
            return None
        stack.append(node.val)
        self.dfs(node.left,stack)
        self.dfs(node.right,stack)
        return None

    def isSameTree2(self, p, q):
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        
        if p.val==q.val:
            return self.isSameTree2(p.left, q.left) and self.isSameTree2(p.right, q.right)
        else:
            return False