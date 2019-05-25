class Solution:
    """
    https://leetcode.com/problems/guess-number-higher-or-lower-ii/

    Solution:
    https://leetcode.com/problems/guess-number-higher-or-lower-ii/discuss/84764/Simple-DP-solution-with-explanation~~/191983
    """
    def getMoneyAmount(self, n: int) -> int:
        dp=[[0 for i in range(n+2)] for j in range(n+2)]
        for i in range(n,0,-1):
            for j in range(i, n+1):
                if i==j:
                    dp[i][j]=0
                else:
                    dp[i][j]=float('inf')
                    for k in range(i,j+1):
                        tmp=k+max(dp[i][k-1], dp[k+1][j])
                        dp[i][j]=min(dp[i][j],tmp)
        return dp[1][n]

        