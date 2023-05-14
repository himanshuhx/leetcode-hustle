class Solution:
    def minSteps(self, n: int) -> int:
        def solve(curr,buffer):
            if curr>n:
                return float("inf")
            if curr==n:
                return 0
            key = (curr,buffer)
            if key in memo:
                return memo[key]
            memo[key] = min(solve(curr+buffer,curr+buffer)+2,solve(curr+buffer,buffer)+1)
            return memo[key]
        if n==1:
            return 0
        memo = {}
        return solve(0,1)