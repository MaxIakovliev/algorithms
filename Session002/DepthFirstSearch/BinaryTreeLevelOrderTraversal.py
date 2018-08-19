class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result=[]
        nextLevel=[]
        if root is None:
            return result
        result.append([root.val])
        nextLevel.append(root.left)
        nextLevel.append(root.right)
        currentLevel=nextLevel
        nextLevel=[]
        tmp=[]
        while len(currentLevel)>0:
            cur=currentLevel.pop(0)
            if cur is not None:
                if cur.val is not None:
                    tmp.append(cur.val)
                nextLevel.append(cur.left)
                nextLevel.append(cur.right)
            if len(currentLevel)==0:
                if len(tmp)>0:
                    result.append(tmp)
                tmp=[]
                currentLevel=nextLevel
                nextLevel=[]

        if len(tmp)>0:
            result.append(tmp)
        return result
            

        