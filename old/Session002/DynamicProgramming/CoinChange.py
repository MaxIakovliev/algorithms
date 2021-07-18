class Solution(object):
    """
    https://leetcode.com/problems/coin-change/
    """
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp=[amount+1 for _ in range(amount+1)]
        dp[0]=0
        for i in range(1, amount+1):
            for c in coins:
                if i>=c:
                    dp[i]=min(dp[i-c]+1, dp[i])
        if dp[amount]==amount+1:
            return -1
        return dp[amount]

        