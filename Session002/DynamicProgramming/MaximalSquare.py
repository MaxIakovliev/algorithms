class Solution:
    """
    https://leetcode.com/problems/maximal-square/
    """
    def maximalSquare(self, matrix: 'List[List[str]]') -> int:
        if len(matrix)==0:
            return 0
        m=len(matrix)
        n=len(matrix[0])
        dp=[[0 for i in range(n+1)] for _ in range(m+1)]
        res=0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1]=='0':
                    continue
                dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                res=max(dp[i][j], res)
        return res*res
if __name__ == "__main__":
    c=Solution()
    print(c.maximalSquare(
        [
["1","0","1","0","0"],
["1","0","1","1","1"],
["1","1","1","1","1"],
["1","0","0","1","0"]
        ]
))
        
        