# vvimp https://www.youtube.com/watch?v=lXVy6YWFcRM
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = max(nums)
        currMin, currMax = 1, 1
        for n in nums:
            if n!=0:
                temp = currMax
                currMax = max(currMax*n,currMin*n,n)
                currMin = min(temp*n,currMin*n,n)
                maxi = max(maxi,currMax)
            else:
                currMin, currMax = 1, 1
        return maxi