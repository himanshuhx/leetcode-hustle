'''
binary search + sliding window
will analyze again after doing sliding window
Time complexity - O(nlogN) + O(nlog(max(nums)-min(nums))) 
sorting + binary search (0 to max distance)
'''
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        def feasible(distance):
            count, n = 0, len(nums)
            i, j = 0, 0
            while i<n or j<n:
                while j<n and nums[j]-nums[i]<=distance:
                    j+=1
                count += j-i-1
                i+=1
            return count>=k
            
        nums.sort()   
        left, right = 0, nums[-1]-nums[0]
        while left<right:
            mid = left + (right-left)//2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left