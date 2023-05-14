class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def valid(i,j, wIdx):
            if i>=0 and j>=0 and i<m and j<n and board[i][j]==word[wIdx]:
                return True
            return False
        
        def dfs(i, j, wIdx):
            if wIdx>=len(word):
                return True
            if not valid(i,j,wIdx):
                return False
            
            temp, board[i][j] = board[i][j], "*"
            
            for x, y in [[-1,0], [0,-1], [1,0], [0,1]]:
                newX, newY = x+i, y+j
                if dfs(newX,newY,wIdx+1):
                        return True
                    
            board[i][j] = temp
            return False
        
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if dfs(i,j,0):
                        return True
        return False
        