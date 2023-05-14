class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def solve(i,j):
            if i>=len(s) and j>=len(p):
                return True
            if i>=len(s):
                while j!=len(p):
                    if p[j]!='*':
                        return False
                    j+=1
                return True
            if j>=len(p):
                return False
            key = (i,j)
            if key in memo:
                return memo[key]
            match = (s[i]==p[j] or p[j]=='?')  l;

            
            if p[j]=='*':
                memo[key] = (solve(i+1,j) or solve(i,j+1) or solve(i+1,j+1))
                return memo[key]
            if match:
                memo[key] = solve(i+1,j+1)
                return memo[key]
            memo[key] = False
            return memo[key]
        
        memo = {}
        return solve(0,0)