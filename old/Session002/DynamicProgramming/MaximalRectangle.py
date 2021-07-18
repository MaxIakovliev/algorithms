class Solution:
    """
    https://leetcode.com/problems/maximal-rectangle/
    solution:
    https://leetcode.com/problems/maximal-rectangle/discuss/29054/Share-my-DP-solution
    """
    def maximalRectangle(self, matrix: 'List[List[str]]') -> int:
        if len(matrix)==0:
            return 0
        m=len(matrix)
        n=len(matrix[0])
        left=[0 for i in range(n)]
        right=[n for i in range(n)]
        height=[0 for i in range(n)]
        max_a=0
        for i in range(m):
            cur_left=0
            cur_right=n
            for j in range(n):
                if matrix[i][j]=='1':
                    height[j]+=1
                else:
                    height[j]=0

            for j in range(n):
                if matrix[i][j]=='1':
                    left[j]=max(cur_left,left[j])
                else:
                    left[j]=0
                    cur_left=j+1
            
            for j in range(n-1,-1,-1):
                if matrix[i][j]=='1':
                    right[j]=min(right[j], cur_right)
                else:
                    right[j]=n
                    cur_right=j
            
            for j in range(n):
                max_a=max(max_a,(right[j]-left[j])*height[j])

        return max_a
if __name__ == "__main__":
    c=Solution()
    print(c.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])) #6



            

        


        