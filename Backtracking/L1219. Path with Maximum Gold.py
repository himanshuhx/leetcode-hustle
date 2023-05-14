# Time complexity is O(mn)*(4^(mn)), O(mn)

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
            
        def possible(i,j):
            if i<m and j<n and i>=0 and j>=0 and grid[i][j]!=0:
                return True  
            return False
        
        def solve(i,j):
            if not possible(i,j):
                return 0
            gold = 0
            for x, y in [[-1,0],[1,0],[0,-1],[0,1]]:
                newX, newY = x+i, y+j
                temp, grid[i][j] = grid[i][j], 0
                gold = max(gold, solve(newX,newY)+temp)
                grid[i][j] = temp
                    
            return gold
                    
        
        m, n = len(grid), len(grid[0])
        maxi = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=0:
                    maxi = max(maxi, solve(i,j))          
        return maxi