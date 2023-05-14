class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def valid(x, y, num):
            for i in range(m):
                if board[i][y]==num:
                    return False
            for j in range(n):
                if board[x][j]==num:
                    return False
            gridI, gridY = (x//3)*3, (y//3)*3
            for i in range(3):
                for j in range(3):
                    if board[gridI+i][gridY+j]==num:
                        return False                    
            return True
            
        def solve(i, j):
            if i == m:
                return True
            
            nextI, nextJ = 0, 0
            if j==n-1:
                nextI, nextJ = i+1, 0
            else:
                nextI, nextJ = i, j+1
            
            if board[i][j] != ".":
                return solve(nextI, nextJ)
            else:
                for num in range(1,10):
                    if valid(i, j, str(num)):
                        board[i][j] = str(num)
                        if solve(nextI, nextJ): return True
                        board[i][j] = "."
                return False
        
        m, n = len(board), len(board[0])
        solve(0, 0)


        