class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        def solve(n,summ):
            if n<0 and summ==0:
                return 1
            if n<0 and summ!=0:
                return 0
            key = (n,summ)
            if key in memo:
                return memo[key]
            memo[key] = solve(n-1,summ-nums[n])+solve(n-1,summ+nums[n])
            return memo[key]
        
        memo = {}
        return solve(len(nums)-1,S)