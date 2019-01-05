class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def dfs(a,b):
            if a is None and b is None:
                return True
            if a is None or b is None:
                return False

            return a.val==b.val and dfs(a.left, b.left) and dfs(a.right, b.right)

        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        
        return dfs(s,t) or dfs(s.left, t) or dfs(s.right,t)