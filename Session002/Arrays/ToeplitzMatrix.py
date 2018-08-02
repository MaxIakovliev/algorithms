class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for  i in range(len(matrix)):
            if self.check(matrix,i,0,matrix[i][0])==False:
                return False
        for i in range(len(matrix[0])):
            if self.check(matrix,0,i,matrix[0][i])==False:
                return False
        return True
    
    def check(self, a, x,y, exp):
        xlen=len(a)
        ylen=len(a[0])
        while x<xlen and y<ylen:
            if a[x][y]!=exp:
                return False
            x+=1
            y+=1
        return True
            
if __name__ == "__main__":
    c=Solution()
    matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
    print(c.isToeplitzMatrix(matrix))

    matrix = [
  [1,2],
  [2,2]
]
    print(c.isToeplitzMatrix(matrix))
    