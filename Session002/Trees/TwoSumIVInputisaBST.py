class Solution:
    """
    https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
    """
    def findTarget(self, root, k: int) -> bool:
        def dfs(node, target):
            if node is None:
                return
            dfs(node.left, target)
            dfs(node.right,target)
            t=target - node.val
            if t in self.d:
                self.result=True
                return
            self.d.add(node.val)
            return
        self.d=set()
        self.result=False
        dfs(root,k)
        return self.result



        