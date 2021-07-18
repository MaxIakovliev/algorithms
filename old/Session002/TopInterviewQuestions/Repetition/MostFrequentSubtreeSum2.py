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
        def dfs(node,data):
            if node is None:
                return 0
            left=dfs(node.left,data)  #traverse left sub tree
            right=dfs(node.right,data)#traverse right sub tree
            currentVal=left+right+node.val # sum value of current sub tree

            if currentVal in data:
                data[currentVal]+=1 #increment existing value
            else:
                data[currentVal]=0 # set 0 for our convenience

            self.maxSoFar=max(self.maxSoFar,data[currentVal]) # update local max value
            return currentVal

        #main block of code

        result=[] #result :)
        data={}
        self.maxSoFar=0 # init with 0 for our convenience
        dfs(root,data) #traverse tree
        for k,v, in data.items():
            if v==self.maxSoFar:
                result.append(k)
        
        return result 

 




        



