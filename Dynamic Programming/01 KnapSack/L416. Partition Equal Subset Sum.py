class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def solve(n, targetSum):
            if n<0 and targetSum!=0:
                return False
            if targetSum==0:
                return True
            key = (n, targetSum)
            if key in memo:
                return memo[key]
            if nums[n]<=targetSum:
                memo[key] = solve(n-1,targetSum-nums[n]) or solve(n-1,targetSum)
            else:
                memo[key] = solve(n-1,targetSum)
            return memo[key]
            
        total = sum(nums)
        if total%2!=0:
            return False
        memo = {}
        return solve(len(nums)-1, total//2)
        