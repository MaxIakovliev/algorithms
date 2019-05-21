class Solution(object):
    """
    https://leetcode.com/problems/burst-balloons/
    solution:
    https://leetcode.com/problems/burst-balloons/discuss/76228/Share-some-analysis-and-explanations
    """
    def maxCoins(self, i_nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + [x for x in i_nums if x > 0] + [1]
        n=len(nums)
        dp=[[0 for i in range(n)] for _ in range(n)]
        for k in range(2, n):
            for left in range(0, n - k):
                right = left + k
                for i in range(left + 1,right):
                    dp[left][right] = max(dp[left][right],
                        nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
        return dp[0][n - 1]        


        