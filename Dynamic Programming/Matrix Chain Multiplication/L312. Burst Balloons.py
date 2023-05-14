class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def solve(i,j):
            if i>=j:
                return 0
            key = (i,j)
            if key in memo:
                return memo[key]
            maxi = -float("inf")
            
            for k in range(i,j):
                temp = solve(i,k) + solve(k+1,j) + nums[i-1]*nums[k]*nums[j]
                maxi = max(maxi,temp)
            memo[key] = maxi
            return memo[key]
        
        memo = {}
        nums.append(1)
        nums.insert(0,1)
        return solve(1,len(nums)-1)