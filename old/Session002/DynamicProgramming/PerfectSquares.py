class Solution:
    """
    https://leetcode.com/problems/perfect-squares/
    solution:
    https://leetcode.com/problems/perfect-squares/discuss/71587/Explanation-of-the-DP-solution
    """
    def numSquares(self, n: int) -> int:
        dp=[0 for _ in range(n+1)]
        for i in range(1, n+1):
            j=1
            min_val=float('inf')
            while j*j<=i:
                min_val=min(dp[i-j*j]+1, min_val)
                j+=1
            dp[i]=min_val
        return dp[-1]
if __name__ == "__main__":
    c=Solution()
    print(c.numSquares(12))#3
    print(c.numSquares(13))#2

        