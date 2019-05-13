class Solution:
    """
    https://leetcode.com/problems/minimum-score-triangulation-of-polygon/
    Solution:
    https://leetcode.com/problems/minimum-score-triangulation-of-polygon/discuss/286705/JavaC%2B%2BPython-DP
    """
    def minScoreTriangulation(self, A: 'List[int]') -> int:
        """
        Explanation:
        Intuition

The connected two points in polygon shares one common edge,
these two points must be one and only one triangles.


Explanation

dp[i][j] means the minimum score to triangulate A[i] ~ A[j],
while there is edge connect A[i] and A[j].

We enumerate all points A[k] with i < k < j to form a triangle.

The score of this triangulation is dp[i][j], dp[i][k] + dp[k][j] + A[i] * A[j] * A[k]
        """
        n=len(A)
        dp=[[0]*n for _ in range(n)]
        for d in range(2, n):
            i=0
            while i+d<n:
                j=i+d
                dp[i][j]=float('inf')
                for k in range(i+1,j):
                    dp[i][j]=min(dp[i][j], dp[i][k]+dp[k][j]+A[i]*A[j]*A[k])
                i+=1
        return dp[0][-1]
if __name__ == "__main__":
    c=Solution()
    print(c.minScoreTriangulation( [1,2,3]))#6
    print(c.minScoreTriangulation( [3,7,4,5]))#144


