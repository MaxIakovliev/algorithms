# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def post(node,data):
            if node is None:
                return data
            left=post(node.left, data)
            right=post(node.right,data)
            currentSum=left+right+node.val
            if currentSum in data:
                data[currentSum]+=1
            else:
                data[currentSum]=0
            self.maxSoFar=max(self.maxSoFar, data[currentSum])
            return currentSum
        
        self.maxSoFar=0
        data={}
        post(root, data)
        res=[]
        for k,v in data.items():
            if v==self.maxSoFar:
                res.append(k)
        return res