class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i, j = 0, 0
        zeroes, maxi = 0, -float("inf")
        while j<len(nums):
            if nums[j]==0:
                zeroes += 1
            while zeroes>1:
                if nums[i]==0:
                    zeroes-=1
                i+=1
            maxi = max(maxi,j-i)
            j+=1
        return maxi