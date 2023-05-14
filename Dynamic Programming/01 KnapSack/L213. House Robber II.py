class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(n,included):
            if n<0:
                return 0
            if n==0 and included:
                return 0
            if n==0 and not included:
                return nums[0]
            key = (n,included)
            if key in memo:
                return memo[key]
            memo[key] = max(solve(n-2,included)+nums[n],solve(n-1,included))
            return memo[key]
        
        memo = {}
        if len(nums)==1:
            return nums[0]
        return max(solve(len(nums)-1,True),solve(len(nums)-2,False))