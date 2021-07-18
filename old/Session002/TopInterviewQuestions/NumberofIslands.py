class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def check(grid, x,y, num):
            if x>=len(grid) or x<0 or y<0 or y>=len(grid[x]):
                return
            if (str(x)+"_"+str(y)) in q or grid[x][y]!="1":
                return
            else:
                
                q.add(str(x)+"_"+str(y))
                check(grid,x+1,y,num)
                check(grid,x-1,y,num)
                check(grid,x,y-1,num)
                check(grid,x,y+1,num)
        num=0
        q=set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=="1" and (str(i)+"_"+str(j)) not in q:
                    num+=1
                    check(grid, i,j,num)
        return num
if __name__=="__main__":
    c=Solution()
    arr=[
        "11110",
        "11010",
        "11000",
        "00000"
        ]
    print(c.numIslands(arr))

    arr=[
        "11000",
        "11000",
        "00100",
        "00011"
        ]
    print(c.numIslands(arr))
                    

 