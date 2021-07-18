class KnightsTour:
    def __init__(self, board_size):
        self.reset_board(board_size)
        self.size = board_size
    
    def reset_board(self, size):
        self.board = [[-1]*size for i in range(size)]


    def solve(self, x, y, number_of_moves):
        number_of_moves+=1
        self.board[x][y]=number_of_moves

        if number_of_moves==(self.size*self.size):
            return True

        row = [-2, -2, -1, -1,  2, 2, 1, 1]
        col = [-1,  1, -2,  2, -1, 1, 2, -2]

        for i in range(len(row)):
            r=x+row[i]
            c=y+col[i]
            if r>=0 and r<self.size and c>=0 and c<self.size and self.board[r][c]==-1:
                if self.solve(r,c,number_of_moves):
                    return True
        self.board[x][y]=-1
        return False
    
if __name__=="__main__":
    size=6
    c=KnightsTour(size)
    c.solve(0,0,0)
    for i in range(size):
        print(c.board[i])
        # print(s)
       


