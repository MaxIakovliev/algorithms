class Solution:
    def solveNQueens(self, n: int) -> "List[List[str]]":
        def solve(board,col):
            if len(board)==col:
                board_out=[]
                for i in range(len(board)):
                    # board_out.append([])
                    board_out.append(''.join(board[i]))
                self.res.append(board_out)
                return

            result=False
            for i in range(len(board)):
                if isPossible(board,i,col):
                    board[i][col]='Q'
                    result=solve(board,col+1) or result
                    board[i][col]='.'
            return result
        
        def isPossible(board,row,col):
            for i in range(col):
                if board[row][i]=='Q':
                    return False
            
            i,j=row,col
            while i>=0 and j>=0:
                if board[i][j]=='Q':
                    return False
                i-=1
                j-=1

            i,j=row,col
            while j>=0 and i<len(board):
                if board[i][j]=='Q':
                    return False
                i+=1
                j-=1

            return True
        
        board=[['.']*n for i in range(n)]
        self.res=[]
        solve(board,0)
        return self.res

        for i in range(len(self.res)):
            self.printBoard(self.res[i])

    def printBoard(self, board):
        print('[')
        for i in range(len(board)):
            print(board[i])
        print(']')
        print('-'*20)
if __name__=="__main__":
    c=Solution()
    c.solveNQueens(4)

