class Solution:
    """
    https://leetcode.com/problems/dungeon-game/

    solution:
    https://leetcode.com/problems/dungeon-game/discuss/52826/A-very-clean-and-intuitive-solution-(with-explanation)
    """
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m=len(dungeon)
        n=(0 if m==0 else len(dungeon[0]))
        dp=[[0 for i in range(n+1)] for i in range(m+1)]

        for i in range(m+1):
            dp[i][n]=float('inf')

        for i in range(n+1):
            dp[m][i]=float('inf')


        dp[m][n-1]=0
        dp[m-1][n]=0
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j]=max(
                    min(dp[i+1][j], dp[i][j+1]) -dungeon[i][j]
                    ,0 
                )
        return dp[0][0]+1

if __name__ == "__main__":
    c=Solution()
    print(c.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))
