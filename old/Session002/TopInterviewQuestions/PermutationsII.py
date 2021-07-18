class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(arr:list, path,res:list):
            if len(arr)==0:
                key=str(path)
                if key not in u:
                    res.append(path)
                    u.add(key)
            for i in range(len(arr)):
                dfs(arr[:i]+arr[i+1:],path+[arr[i]],res)
        u=set()
        res=list()
        dfs(nums,[],res)
        return res
if __name__=="__main__":
    c=Solution()
    print(c.permute([1,2,1]))