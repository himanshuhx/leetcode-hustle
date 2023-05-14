class Solution:
    def stoneGameIII(self, nums: List[int]) -> str:
        def solve(i):
            if i>=len(nums):
                return 0
            ans = -float("inf")
            
            key = i
            if key in memo:
                return memo[key]
            
            ans = max(ans,nums[i]-solve(i+1))
            if i+1<len(nums):
                ans = max(ans,nums[i]+nums[i+1]-solve(i+2))
            if i+2<len(nums):
                ans = max(ans,nums[i]+nums[i+1]+nums[i+2]-solve(i+3))
            memo[key] = ans
            return memo[key]
        
        memo = {}
        res = solve(0)
        if res<0:
            return "Bob"
        elif res>0:
            return "Alice"
        else:
            return "Tie"