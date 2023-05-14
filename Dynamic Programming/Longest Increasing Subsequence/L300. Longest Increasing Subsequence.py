# https://www.youtube.com/watch?v=cjWnW0hdF1Y
# 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def solve(isEmpty,i,prev):
            if i>=len(nums):
                return 0
            include = 0
            if isEmpty or prev<nums[i]:
                include = 1 + solve(False,i+1,nums[i])
            exclude = solve(isEmpty,i+1,prev)
            return max(include,exclude)
        
        return solve(True,0,nums[0])

    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    LIS[i] = max(LIS[i],1+LIS[j])
        return max(LIS)