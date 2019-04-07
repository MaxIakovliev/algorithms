class Solution:
    def isCousins(self, root, x: int, y: int) -> bool:
        def dfs(node, level,parent,x,y):
            if node is None:
                return 
            dfs(node.left, level+1,  node.val,x,y)
            dfs(node.right, level+1, node.val,x,y)
            if x==node.val:
                self.xlevel=level
                self.xparent=parent
            if y==node.val:
                self.ylevel=level
                self.yparent=parent
            return
        self.xlevel=-1
        self.ylevel=-1
        self.xparent=None
        self.yparent=None
        dfs(root,1,root,x,y)
        if self.xparent!=self.yparent and self.xlevel==self.ylevel:
            return True
        return False

        