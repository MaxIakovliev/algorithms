# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    https://leetcode.com/problems/distribute-coins-in-binary-tree/

    solution:
    https://leetcode.com/problems/distribute-coins-in-binary-tree/discuss/221930/JavaC%2B%2BPython-Recursive-Solution
    """
    def distributeCoins(self, root: 'TreeNode') -> int:
        def dfs(node):
            if node is None:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            self.res+=(abs(left)+abs(right))
            return node.val+left+right-1
        self.res=0
        dfs(root)
        return self.res
        