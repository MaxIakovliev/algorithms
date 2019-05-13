class Solution(object):
    """
    https://leetcode.com/problems/unique-paths-ii/
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        width=len(obstacleGrid[0])
        dp=[0]*(width)
        dp[0]=1
        for row in obstacleGrid:
            for i in range(width):
                if row[i]==1:
                    dp[i]=0
                elif i>0:
                    dp[i]+=dp[i-1]
        return dp[-1]

if __name__ == "__main__":
    c=Solution()
    print(c.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
]))#2

    print(c.uniquePathsWithObstacles([[0]]))


        