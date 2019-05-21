class Solution(object):
    """
    https://leetcode.com/problems/longest-increasing-subsequence/
    soultion: https://leetcode.com/problems/longest-increasing-subsequence/discuss/280324/python-O(n2)-and-O(nlogn)-solutions
    """
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dp=[1 for _ in range(len(nums))]
        # dp = [1] * len(nums)
        res=0
        for i in range(len(nums)):
            for j in range(i-1,-1,-1):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
            res=max(res, dp[i])
        return res
if __name__ == "__main__":
    c=Solution()
    print(c.lengthOfLIS([0]))#1
    print(c.lengthOfLIS([10,9,2,5,3,7,101,18]))#4