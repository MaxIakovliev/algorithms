"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
        https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        return self.dfs(root,1)

    def dfs(self, node, depth):
        if node.children is None or len(node.children)==0:
            return depth
        tmpDepth=depth
        for  i in range(len(node.children)):
            cur=self.dfs(node.children[i],tmpDepth+1)
            depth=max(depth,cur)
        return depth