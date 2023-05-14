'''
array will be given increasing/decreasing like mountain slope we have to find peak of 
mountain (greatest element among array)

three cases can arise ---

1. if element is itself peak than ele just left and right to curr ele will be smaller
2. if we are in climbing mode    
     / --> curr ele              arr[mid]   (greater)
    /  --> ele just left to it   arr[mid-1] (is smaller)
   /
   in this case we have to set our left to "mid+1" as probability to find peak ele is 
   next to curr ele
3. if we are in descending mode    
    \ -->    ele just right to it   arr[mid-1] (is greater)               
     \  -->  curr ele               arr[mid]   (smaller)
      \   
   in this case we have to set our right to "mid-1" as probability to find peak ele is 
   before curr ele
'''
# Time complexity - O(logn)
# Space Complexity - O(1)


class Solution:
    def peakElement(nums, n):
        left, right = 0, n-1
        while left < right-1:  # to handle case where peak can be last index
            mid = left + (right-left)//2
            if nums[mid-1] < nums[mid] and nums[mid+1] < nums[mid]:
                return mid
            elif nums[mid-1] < nums[mid]:
                left = mid+1
            else:
                right = mid-1
        return left if nums[left] >= nums[right] else right

# same as peak element


class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid-1] > nums[mid]:
                right = mid
            else:
                left = mid + 1
        return left-1
