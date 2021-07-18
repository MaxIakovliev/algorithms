class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                cur=0
                if grid[i][j]==1:
                    cur+=1
                    grid[i][j]=2
                    cur+=self.goTop(grid,i,j)
                    cur+=self.goBottom(grid,i,j)
                    cur+=self.goLeft(grid,i,j)
                    cur+=self.gotRight(grid,i,j)
                res=max(cur,res)
        return res

            
        

    def goTop(self, grid, x,y):
        res=0
        while True:
            if y-1>=0 and grid[x][y-1]==1:
                y-=1
                res+=1
                grid[x][y]=2
                res+=self.goLeft(grid,x,y)
                res+=self.gotRight(grid,x,y)
                res+=self.goBottom(grid,x,y)
            else:
                break
        return res

    def goBottom(self, grid, x,y):
        res=0
        while True:
            if y+1<len(grid[x]) and grid[x][y+1]==1:
                y+=1
                res+=1
                grid[x][y]=2
                res+=self.goLeft(grid,x,y)
                res+=self.gotRight(grid,x,y)
                res+=self.goTop(grid,x,y)
            else:
                break
        return res

    def goLeft(self, grid, x,y):
        res=0
        while True:
            if x-1>=0 and grid[x-1][y]==1:
                x-=1
                res+=1
                grid[x][y]=2
                res+=self.goTop(grid, x,y)
                res+=self.goBottom(grid, x,y)
                res+=self.gotRight(grid, x,y)
            else:
                break
        return res
    def gotRight(self, grid, x,y):
        res=0
        while True:
            if x+1<len(grid) and grid[x+1][y]==1:
                x+=1
                res+=1
                grid[x][y]=2
                res+=self.goTop(grid,x,y)
                res+=self.goBottom(grid,x,y)
                res+=self.goLeft(grid,x,y)
            else:
                break
        return res

if __name__=="__main__":
    c=Solution()
    print(c.maxAreaOfIsland([[0,1,0]]))

