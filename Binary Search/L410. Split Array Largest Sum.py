class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        def feasible(threshold):
            count, currSum = 1, 0
            for num in nums:
                currSum += num
                if currSum > threshold:
                    currSum = num
                    count += 1
                if count > m:
                    return False
            return True
        
        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left)//2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
        