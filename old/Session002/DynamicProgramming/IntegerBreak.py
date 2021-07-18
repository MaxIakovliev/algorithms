class Solution(object):
    """
    https://leetcode.com/problems/integer-break/
    solution:
    https://leetcode.com/problems/integer-break/discuss/80694/Java-DP-solution
    """
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0 for _ in range(n+1)]
        dp[1]=1
        for i in range(2, n+1):
            for j in range(1,i):
                dp[i]=max(dp[i],max(j,dp[j])*max(i-j,dp[i-j]))
        return dp[n]
if __name__ == "__main__":
    c=Solution()
    print(c.integerBreak(10))#36
