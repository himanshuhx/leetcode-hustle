class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def feasible(currDivisor):
            currSum = 0
            for num in nums:
                currSum += (num-1)//currDivisor + 1
            return currSum <= threshold
            
        left, right = 1, max(nums)
        while left < right:
            mid = left + (right - left)//2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1        
        return left
        