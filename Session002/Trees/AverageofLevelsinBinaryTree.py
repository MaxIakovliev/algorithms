class Solution:
    """
    https://leetcode.com/problems/average-of-levels-in-binary-tree/
    """
    def averageOfLevels(self, root: "TreeNode") -> "List[float]":
        def dfs(node, level):
            if node is None:
                return
            if level>len(self.tmp):
                self.tmp.append([])
            self.tmp[level].append(node.val)
            dfs(node.left,level+1)
            dfs(node.right, level+1)
            return
        self.tmp=[]
        dfs(root,1)
        res=[]
        for i in range(len(self.tmp)):
            sval=0
            for j in range(len(self.tmp[i])):
                sval+=self.tmp[i][j]
            res.append(sval/len(self.tmp[i]))
        return res

        