class Solution:
    """
    https://leetcode.com/problems/battleships-in-a-board/
    """
    def countBattleships(self, board: 'List[List[str]]') -> int:
        def dfs(arr,i,j):
            if i>=0 and j>=0 and i<len(arr) and j<len(arr[0]) and arr[i][j]=='X':
                arr[i][j]='.'
                dfs(arr,i-1,j)
                dfs(arr,i+1,j)
                dfs(arr,i,j-1)
                dfs(arr,i,j+1)
        res=0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='X':
                    dfs(board,i,j)
                    res+=1
        return res
if __name__ == "__main__":
    c=Solution()
    print(c.countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]))