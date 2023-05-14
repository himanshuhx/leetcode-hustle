class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        zeroes, maxi = 0, -float("inf")
        while j<len(nums):
            if nums[j]==0:
                zeroes += 1
            while zeroes>k:
                if nums[i]==0:
                    zeroes-=1
                i+=1
            maxi = max(maxi, j-i+1)
            j+=1
        return maxi