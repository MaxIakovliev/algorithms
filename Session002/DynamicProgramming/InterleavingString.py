class Solution:
    """
    https://leetcode.com/problems/interleaving-string/
    solution:
    https://leetcode.com/problems/interleaving-string/discuss/278192/python3-DPsolution
    """
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m=len(s1)
        n=len(s2)
        if m+n!=len(s3):
            return False
        dp=[[False for i in range(n+1)] for _ in range(m+1)]

        dp[0][0]=True
        for i in range(1, m+1):
            dp[i][0]=s1[i-1]==s3[i-1] and dp[i-1][0]

        for i in range(1, n+1):
            dp[0][i]=s2[i-1]==s3[i-1] and dp[0][i-1]
        
        for i in range(1, m+1):
            for j in range(1,n+1):
                dp[i][j]=(dp[i-1][j] and s1[i-1]==s3[i+j-1]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1])
        
        return dp[-1][-1]



