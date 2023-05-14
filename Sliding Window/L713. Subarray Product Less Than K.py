# whenever there is a question asking about number of subarrays we can just change
# the maxi = max(maxi,j-i+1) part of template to maxi += j-i+1

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        i, j = 0, 0
        maxi, currWindowPro = 0, 1
        while j<len(nums):
            currWindowPro *= nums[j]
            while currWindowPro>=k:
                currWindowPro /= nums[i]
                i+=1
            maxi += j-i+1
            j+=1
        return maxi