class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        def solve(n,m):
            if n<0 or m<0:
                return 0
            key = (n,m)
            if key in memo:
                return memo[key]
            if s1[n]==s2[m]:
                memo[key] = 1+solve(n-1,m-1)
            else:
                memo[key] = max(solve(n-1,m),solve(n,m-1))
            return memo[key]
        
        memo = {}   
        return solve(len(s1)-1,len(s2)-1)