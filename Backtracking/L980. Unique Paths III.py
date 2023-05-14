class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def valid(i, j):
            if i>=0 and j>=0 and i<m and j<n and grid[i][j]!=-1:
                return True
            return False
        
        def getNoOfPaths(i, j, validSq):
            if not valid(i,j):
                return
            
            validSq += 1

            if grid[i][j]==2 and validSq==walkableSq:
                self.count += 1
                return
            
            temp, grid[i][j] = grid[i][j], -1
            for x, y in [[-1,0],[1,0],[0,1],[0,-1]]:
                newX, newY = x+i, y+j
                getNoOfPaths(newX,newY, validSq)
            grid[i][j] = temp
        
        
        m , n = len(grid), len(grid[0])
        self.count = 0
        startI, startJ, walkableSq = 0, 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    startI, startJ = i, j
                if grid[i][j]!=-1:
                    walkableSq += 1
                    
        getNoOfPaths(startI, startJ, 0)
        return self.count