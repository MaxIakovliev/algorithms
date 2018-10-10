# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root):
        def post(node):
            if node is None:
                return 0
            left=post(node.left)
            right=post(node.right)
            curSum=left+right+node.val
            if curSum in data:
                data[curSum]+=1
            else:
                data[curSum]=0
            self.maxVal=max(self.maxVal, data[curSum])
            return curSum


        self.maxVal=0
        data=dict()
        res=list()
        post(root)
        for k,v in data.items():
            if v==self.maxVal:
                res.append(k)
        return res



