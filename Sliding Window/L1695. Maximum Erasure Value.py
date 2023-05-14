class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        i , j = 0, 0                            
        currWindowSum, count, maxi = 0, {}, -float("inf")
        while j<len(nums):
            if nums[j] in count:
                count[nums[j]] += 1
            else:
                count[nums[j]] = 1
            currWindowSum += nums[j]
           
            while count[nums[j]]>1:
                count[nums[i]] -= 1
                currWindowSum -= nums[i]
                i+=1
            
            maxi = max(maxi,currWindowSum)
            j+=1
        return maxi