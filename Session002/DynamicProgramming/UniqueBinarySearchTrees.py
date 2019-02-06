class Solution:
    """
    https://leetcode.com/problems/unique-binary-search-trees/

    """
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0]*(n+1)
        dp[0]=dp[1]=1
        for i in range(2, n+1):
            dp[i]=0
            for j in range(1, i+1):
                dp[i]+=dp[j-1]*dp[i-j]
        
        return dp[n]
        