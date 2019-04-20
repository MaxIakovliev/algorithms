class Solution:
    """
    https://leetcode.com/problems/max-increase-to-keep-city-skyline/
    """
    def maxIncreaseKeepingSkyline(self, grid: 'List[List[int]]') -> int:
        n=len(grid)
        row=[0]*n
        col=[0]*n
        for i in range(n):
            for j in range(n):
                row[i]=max(row[i],grid[i][j])
                col[j]=max(col[j],grid[i][j])
        res=0
        for i in range(n):
            for j in range(n):
                res+=min(row[i],col[j])-grid[i][j]
        return res

if __name__ == "__main__":
    c=Solution()
    print(c.maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))#35
        