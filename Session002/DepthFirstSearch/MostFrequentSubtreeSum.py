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