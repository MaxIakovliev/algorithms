# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    3
   / \
  9  20
    /  \
   15   7
    """
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder is None or len(inorder)==0 or postorder is None or len(postorder)==0:
            return
        idx=self.search(inorder, postorder.pop())
        root=TreeNode(inorder[idx])
        root.left=self.buildTree(inorder[:idx],postorder)
        root.right=self.buildTree(inorder[idx+1:],postorder)
        return root

    def buildTree2(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        
        root = TreeNode(postorder.pop())
        inorderIndex = inorder.index(root.val)

        root.right = self.buildTree(inorder[inorderIndex+1:], postorder)
        root.left = self.buildTree(inorder[:inorderIndex], postorder)

        return root

    def search(self, data, val):
        for i in range(len(data)):
            if data[i]==val:
                return i