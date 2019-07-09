class Solution:
    """
    https://leetcode.com/problems/2-keys-keyboard/
    
    solution:
    https://leetcode.com/problems/2-keys-keyboard/discuss/292658/Python-DP-simple.
    """
    def minSteps(self, n: int) -> int:
        dp=[float('inf')]*(n+1)
        dp[1]=0
        for i in range(2, n+1):
            for j in range(1, i//2+1):
                if (i-j)%j==0:
                    dp[i]=min(dp[i],dp[j]+((i-j)//j)+1)
        return dp[n]

        