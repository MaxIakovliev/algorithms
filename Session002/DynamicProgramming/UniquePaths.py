class Solution:
    """
    https://leetcode.com/problems/unique-paths/discuss/
    """
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        memo=[[0]*(m)]*(n)
        for i in range(n):
            for j in range(m):
                if i==0 or j==0:
                    memo[i][j]=1
                else:
                    memo[i][j]=memo[i][j-1]+memo[i-1][j]
        return memo[n-1][m-1]

if __name__=="__main__":
    c=Solution()
    print(c.uniquePaths(3,2))

        