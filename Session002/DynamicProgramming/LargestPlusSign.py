class Solution:
    """
    https://leetcode.com/problems/largest-plus-sign/
    
    solution:
    https://leetcode.com/problems/largest-plus-sign/discuss/303187/stupid-solution
    """
    def orderOfLargestPlusSign(self, N: int, mines: 'List[List[int]]') -> int:
        matrix = [[1]*N for i in range(N)]
        for x, y in mines:
            matrix[x][y] = 0

        left_matrx = [[0]*N for _ in range(N)]
        right_matrx = [[0]*N for _ in range(N)]
        up_matrx = [[0]*N for _ in range(N)]
        down_matrx = [[0]*N for _ in range(N)]

        for i in range(len(matrix)):
            count = 0
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    count = 0
                else:
                    count += 1
                left_matrx[i][j] = count

        for i in range(len(matrix)):
            count = 0
            for j in range(len(matrix[0])-1, -1, -1):
                if matrix[i][j] == 0:
                    count = 0
                else:
                    count += 1
                right_matrx[i][j] = count

        for j in range(len(matrix[0])):
            count = 0
            for i in range(len(matrix)):
                if matrix[i][j] == 0:
                    count = 0
                else:
                    count += 1
                up_matrx[i][j] = count

        for j in range(len(matrix[0])):
            count=0
            for i in range(len(matrix)-1, -1, -1):
                if matrix[i][j] == 0:
                    count = 0
                else:
                    count += 1
                down_matrx[i][j] = count

        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, min(
                    left_matrx[i][j], right_matrx[i][j], up_matrx[i][j], down_matrx[i][j]))

        return res





        
