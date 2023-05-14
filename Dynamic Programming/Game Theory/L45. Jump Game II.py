class Solution:
    def jump(self, nums: List[int]) -> int:
        def solve(i):
            if i==len(nums)-1:
                return 0
            if i>=len(nums):
                return float("inf")
            key = i
            if key in memo:
                return memo[key]
            
            mini = float("inf")
            for j in range(1,nums[i]+1):
                temp = solve(i+j)+1
                mini = min(temp,mini)
                
            memo[key] = mini
            return mini
        
        memo = {}
        return solve(0)