class Solution:
    def minCut(self, s: str) -> int:
        def isPali(i,j):
            while i<=j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1                
            return True
                
        def solve(i,j):
            if i>=j:
                return 0
            if isPali(i,j):
                return 0
            
            key = (i,j)
            if key in memo:
                return memo[key]
            
            mini = float("inf")
            for k in range(i,j):
                temp = solve(i,k) + solve(k+1,j) + 1
                mini = min(mini,temp)
            memo[key]=mini
            return memo[key]
        
        memo = {}
        return solve(0,len(s)-1)