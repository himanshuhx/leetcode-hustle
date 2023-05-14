class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def solve(r):
            if r==n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                
            for c in range(n):
                if c in col or r+c in posDiagonal or r-c in negDiagonal:
                    continue
                posDiagonal.add(r+c)
                negDiagonal.add(r-c)
                col.add(c)
                
                board[r][c] = "Q"
                
                solve(r+1)
                
                posDiagonal.remove(r+c)
                negDiagonal.remove(r-c)
                col.remove(c)
                
                board[r][c] = "."       
        res = []
        
        col = set() 
        posDiagonal = set() # row+col
        negDiagonal = set() # row-col

        board = [["."]*n for i in range(n)]
        solve(0)
        return res