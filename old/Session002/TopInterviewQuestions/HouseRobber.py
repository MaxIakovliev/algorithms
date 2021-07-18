class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def dp(arr, i):
            if i<0:
                return 0
            if self.memo[i]>=0:
                return self.memo[i]
            res=max(dp(arr,i-2)+arr[i], dp(arr,i-1))
            self.memo[i]=res
            return res

        self.memo=[-1]*(len(nums)+1)
        return dp(nums, len(nums)-1)
