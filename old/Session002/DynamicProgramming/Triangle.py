class Solution:
    """
    https://leetcode.com/problems/triangle/
    solution:
    https://leetcode.com/problems/triangle/discuss/38724/7-lines-neat-Java-Solution
    """
    def minimumTotal(self, triangle: 'List[List[int]]') -> int:
        dp=[0 for i in range(len(triangle)+1)]
        for i in range(len(triangle)-1,-1,-1):
            for j in range(len(triangle[i])):
                dp[j]=min(dp[j],dp[j+1])+triangle[i][j]
        return dp[0]
if __name__ == "__main__":
    c=Solution()
    print(c.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))#11
        