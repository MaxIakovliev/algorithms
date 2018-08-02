class Solution:
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m = len(s1)
        n = len(s2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        j=1
        while j<=n:
            dp[0][j] = dp[0][j-1]+ord(s2[j-1])
            j+=1
        
        i=1
        while i<=m:
            dp[i][0] = dp[i-1][0]+ord(s1[i-1])
            j=1
            while j<=n:
                if s1[i-1] != s2[j-1]:
                    dp[i][j] = min(dp[i-1][j]+ord(s1[i-1]), dp[i][j-1]+ord(s2[j-1]))
                else:
                    dp[i][j]=dp[i-1][j-1]
                j+=1
            i+=1
        return dp[m][n]


    def minimumDeleteSum2(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
            for j in range(1, len(s2) + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1] + ord(s2[j - 1]), dp[i - 1][j] + ord(s1[i - 1]))

        return dp[-1][-1]

if __name__ =="__main__":
    c=Solution()
    print(c.minimumDeleteSum("sea","eat"))
    print(c.minimumDeleteSum("delete","leet"))

