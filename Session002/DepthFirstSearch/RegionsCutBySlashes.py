class Solution:
    """
    https://leetcode.com/problems/regions-cut-by-slashes/
    solution:
    https://leetcode.com/problems/regions-cut-by-slashes/discuss/205674/C%2B%2B-with-picture-DFS-on-upscaled-grid
    """

    def regionsBySlashes(self, grid: 'List[str]') -> int:
        def dfs(arr, i,j):
            if i>=0 and j>=0 and i<len(arr) and j<len(arr) and arr[i][j]==0:
                arr[i][j]=1
                dfs(arr,i-1,j)
                dfs(arr,i+1,j)
                dfs(arr,i,j-1)
                dfs(arr,i,j+1)

        #using upscaling - for solving this problem
        g = [[0]*len(grid)*3 for _ in range(len(grid)*3)] #upscale original array by 3
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j]=='/':
                    g[i*3][j*3+2]=g[i*3+1][j*3+1]=g[i*3+2][j*3]=1
                elif grid[i][j]=='\\':
                    g[i*3][j*3]=g[i*3+1][j*3+1]=g[i*3+2][j*3+2]=1

        areas=0
        for i in range(len(g)):
            for j in range(len(g)):
                if g[i][j]==0:
                    dfs(g,i,j)
                    areas+=1

        return areas

