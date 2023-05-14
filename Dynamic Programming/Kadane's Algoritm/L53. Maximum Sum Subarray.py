class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        sum = 0 
        for i in range(len(nums)):
            sum += nums[i]
            maxSum = max(maxSum, sum)
            if sum<0:
                sum=0
        return maxSum
        