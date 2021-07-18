# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    https://leetcode.com/problems/unique-binary-search-trees-ii/
    solution:
    https://leetcode.com/problems/unique-binary-search-trees-ii/discuss/31592/Recursive-python-solution
    """
    def generateTrees(self, n: int) -> 'List[TreeNode]':
        def dfs(start, end):
            if start==end:
                return None
            res=[]
            for i in range(start,end):
                for l in dfs(start,i) or [None]:
                    for r in dfs(i+1, end) or [None]:
                        node=TreeNode(i)
                        node.left,node.right=l,r
                        res.append(node)
            return res
        if n==0:
            return []
        return dfs(1,n+1)

if __name__ == "__main__":
    c=Solution()
    print(c.generateTrees(3))

        