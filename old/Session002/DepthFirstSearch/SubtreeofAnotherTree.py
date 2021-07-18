class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if t is None or s is None:
            return False
        return self.dfs(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t) 

        
    
    def dfs(self, s,t):
        if s is None and  t is None:
            return True
        elif s is None or t is None:
            return False
        elif s.val==t.val:
            return self.dfs(s.left, t.left) and self.dfs(s.right, t.right)
        return False

        
        
