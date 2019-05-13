class Solution:
    """
    https://leetcode.com/problems/rotate-image/
    """
    def rotate(self, matrix: "List[List[int]]") -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        if n<=1:
            return

        start_row=0
        end_row=len(matrix)-1
        start_col=0
        end_col=len(matrix[0])-1

        while start_row<end_row:
            i=0
            while i+start_row<end_row:
                tmp=matrix[start_row][start_col+i]
                matrix[start_row][start_col+i]=matrix[end_row-i][start_col]
                matrix[end_row-i][start_col]=matrix[end_row][end_col-i]
                matrix[end_row][end_col-i]=matrix[start_row+i][end_col]
                matrix[start_row+i][end_col]=tmp
                i+=1
            start_row+=1
            end_row-=1
            start_col+=1
            end_col-=1



            

        