import math
class Solution:
    def findBestValue(self, nums: List[int], target: int) -> int:
        
        def feasible(num):
            total = 0
            for i in range(len(nums)):
                if nums[i]>=num:
                    total+=num
                else:
                    total+=nums[i]
            return total
        
        left, right = 1, max(nums)
        while left < right:
            mid = left + (right - left)//2
            ans = mid
            if feasible(mid)>=target:
                right = mid
            else:
                left = mid + 1
        if abs(feasible(left)-target) < abs(feasible(left-1)-target):
            return left
        return left-1
        