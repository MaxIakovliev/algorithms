class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(arr:list, path,res:list):
            if len(arr)==0:
                res.append(path)
            for i in range(len(arr)):
                dfs(arr[:i]+arr[i+1:],path+[arr[i]],res)
        res=list()
        dfs(nums,[],res)
        return res
if __name__=="__main__":
    c=Solution()
    print(c.permute([1,2,3]))