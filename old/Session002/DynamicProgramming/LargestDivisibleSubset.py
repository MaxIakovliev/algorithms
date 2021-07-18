class Solution:
    """
    https://leetcode.com/problems/largest-divisible-subset/
    Solution:
    https://leetcode.com/problems/largest-divisible-subset/discuss/84006/Classic-DP-solution-similar-to-LIS-O(n2)
    """
    def largestDivisibleSubset(self, nums: "List[int]") -> "List[int]":
        n=len(nums)
        counts=[0 for _ in range(n)]
        pre=[0 for _ in range(n)]
        nums.sort()
        max_val=0
        idx=-1
        for i in range(n):
            counts[i]=1
            pre[i]=-1
            for j in range(i-1,-1,-1):
                if nums[i]%nums[j]==0:
                    if(1+counts[j]>counts[i]):
                        counts[i]=counts[j]+1
                        pre[i]=j
            
            if counts[i]>max_val:
                max_val=counts[i]
                idx=i
            res=[]
        while idx!=-1:
            res.append(nums[idx])
            idx=pre[idx]
            
        return res
        