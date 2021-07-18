# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
   
    """
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode    
        """
        if inorder is None or len(inorder)==0:
            return
        idx= self.getIndx(inorder,preorder.pop(0))
        if idx==-1:
            return
        root=TreeNode(inorder[idx])
        root.left=self.buildTree(preorder,inorder[:idx])
        root.right=self.buildTree(preorder,inorder[idx+1:])
        return root
        
    def getIndx(self, data, val):
        for i in range(len(data)):
            if data[i]==val:
                return i
        return -1

   

