# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.maxVal=0
        data={}
        self.post(root,data)
        res=list()
        for k,v in data.items():
            if v==self.maxVal:
                res.append(k)
        return res
    
    def post(self, node, data):
        if node is None:
            return 0
        
        left=self.post(node.left,data)
        right=self.post(node.right,data)
        curSum=left+right+node.val
        if curSum in data:
            data[curSum]+=1
        else:
            data[curSum]=0
        self.maxVal=max(self.maxVal, data[curSum])
        return curSum

    def findFrequentTreeSum2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """        
        def dfs(node, data):
            if node is None:
                return 0
            left=dfs(node.left, data)
            right=dfs(node.right,data)
            curVal=left+right+node.val
            if curVal in data:
                data[curVal]+=1
            else: 
                data[curVal]=0
            self.maxSoFar=max(self.maxSoFar, data[curVal])
            return curVal
        
        self.maxSoFar=0
        data={}
        dfs(root, data)
        res=[]
        for k,v in data.items():
            if self.maxSoFar==v:
                res.append(k)
        return res


    def findFrequentTreeSum3(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """          
        def dfs(node):
            if node is None:
                return 0
            l=dfs(node.left)
            r=dfs(node.right)
            cur=l+r+node.val
            if cur in self.vals:
                self.vals[cur]+=1
            else:
                self.vals[cur]=0
            self.maxVal=max(self.maxVal, self.vals[cur])
            return cur
        
        self.maxVal=0
        self.vals={}
        res=[]
        dfs(root)
        for k,v in self.vals.items():
            if v ==self.maxVal:
                res.append(k)
        return res
