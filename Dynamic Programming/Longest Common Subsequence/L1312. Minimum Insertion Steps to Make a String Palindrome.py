# min no of insertion or deletion both codes are same
class Solution:
    def minInsertions(self, s: str) -> int:
        def solve(n,m):
            if n<0 or m<0:
                return 0
            key = (n,m)
            if key in memo:
                return memo[key]
            if s[n]==t[m]:
                memo[key] = 1+solve(n-1,m-1)
            else:
                memo[key] = max(solve(n-1,m),solve(n,m-1))
            return memo[key]
        
        memo = {}   
        t=s[::-1]
        lps =  solve(len(s)-1,len(t)-1)
        insertions = len(s)-lps
        return insertions