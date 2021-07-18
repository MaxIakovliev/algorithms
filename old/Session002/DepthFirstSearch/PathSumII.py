# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    https://leetcode.com/problems/path-sum-ii/description/
    """
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.res=[]
        cur=[]
        self.dfs(root, cur,0,sum)
        return self.res

    def dfs(self, node, cur:list, curSum, sum):
        if node is None:
            cur=[]
            return None
        cur.append(node.val)
        curSum+=node.val
        if curSum==sum and node.left is None and node.right is None:
            self.res.append(cur)
            cur=[]
            return
        else:
            tmp=list(cur)
            self.dfs(node.left,tmp,curSum,sum)
            
            tmp=list(cur)
            self.dfs(node.right,tmp,curSum,sum)

        return None
            
        