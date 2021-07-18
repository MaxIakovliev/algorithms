class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            cur = 0
            if dp[i-1] > 0:
                cur = dp[i-1]
            dp[i] = nums[i]+cur
            res = max(res, dp[i])
        return res


if __name__ == "__main__":
    c = Solution()
    print(c.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
