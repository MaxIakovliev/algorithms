# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
    solution: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/discuss/254844/Java-O(n)-solution-with-ranges
    """
    def bstFromPreorder(self, preorder: 'List[int]') -> 'TreeNode':
        def construct(arr, start, end):
            if self.idx==len(arr) or arr[self.idx]<start or arr[self.idx]>end:
                return None
            
            val=arr[self.idx]
            self.idx+=1
            root=TreeNode(val)
            root.left=construct(arr, start, val)
            root.right=construct(arr, val,end)
            return root
        self.idx=0

        if preorder is None or len(preorder)==0:
            return None
        return construct(preorder, float('-inf'), float('inf'))




        