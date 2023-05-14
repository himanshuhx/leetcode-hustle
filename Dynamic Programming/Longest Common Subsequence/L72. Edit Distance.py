class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def solve(n,m):
            if m==0:
                return n
            if n==0:
                return m
            key = (n,m)
            if key in memo:
                return memo[key]
            if word1[n-1]==word2[m-1]:
                memo[key] = solve(n-1,m-1)
            else:
                delete = solve(n-1,m)
                insert = solve(n,m-1)
                replace = solve(n-1,m-1)
                memo[key] = 1 + min(delete,insert,replace)
            return memo[key]
        
        memo = {}
        n, m = len(word1), len(word2)
        return solve(n,m)