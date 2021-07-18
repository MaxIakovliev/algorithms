# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    https://leetcode.com/problems/all-possible-full-binary-trees/
    """
    def allPossibleFBT(self, N: int) -> 'List[TreeNode]':
        res=[]
        if N==1:
            res.append(TreeNode(0))
            return res
        N-=1
        for i in range(1,N,2):
            left=self.allPossibleFBT(i)
            right=self.allPossibleFBT(N-i)
            for l in left:
                for r in right:
                    node=TreeNode(0)
                    
                    node.left=l
                    node.right=r
                    res.append(node)

        return res


        
 