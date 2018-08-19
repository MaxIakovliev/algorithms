# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        l1=self.getLeafs(root1)
        l2=self.getLeafs(root2)
        if len(l1)!=len(l2):
            return False
        for i in range(len(l1)):
            if l1[i]!=l2[i]:
                return False
        return True
            
    def getLeafs(self, root):
        res=[]
        q=list()
        q.append(root)
        while len(q)>0:
            cur=q.pop(0)
            if cur.left is None and cur.right is None:
                res.append(cur.val)            
            elif cur.left is not None:
                q.append(cur.left)
            elif cur.right is not None:
                q.append(cur.right)

        return res

if __name__ =="__main__":
    c=Solution()
    
