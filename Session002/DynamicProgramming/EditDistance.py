class Solution:
    """
    https://leetcode.com/problems/edit-distance/
    """
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        dp=[[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(m+1):
            dp[i][0]=i
        for i in range(n+1):
            dp[0][i]=i
        
        for i in range(m):
            for j in range(n):
                if word1[i]==word2[j]:
                    dp[i+1][j+1]=dp[i][j]
                else:
                    a=dp[i][j]
                    b=dp[i+1][j]
                    c=dp[i][j+1]
                    dp[i+1][j+1]=min(a,b,c)+1
        return dp[-1][-1]
if __name__ == "__main__":
    c=Solution()
    print(c.minDistance("horse","ros"))#3
    print(c.minDistance("intention","execution"))#5
        