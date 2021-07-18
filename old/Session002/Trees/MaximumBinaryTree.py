# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    https://leetcode.com/problems/maximum-binary-tree/
    """
    def constructMaximumBinaryTree(self, nums: 'List[int]') -> 'TreeNode':
        if len(nums)==0:
            return None
        
        max_item=max(nums)
        idx=nums.index(max_item)
        root=TreeNode(max_item)
        root.left=self.constructMaximumBinaryTree(nums[:idx])
        root.right=self.constructMaximumBinaryTree(nums[idx+1:])
        return root
        