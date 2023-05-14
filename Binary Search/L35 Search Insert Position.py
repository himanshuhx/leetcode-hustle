'''
need to find the correct index to insert an ele such that nums remain in inc order

three case arises

1. if position is in middle of array somewhere

   its simple --> correct position will be that where nums[mid-1]<target and nums[mid]>target

2. if position is at first index

   in this case if we apply above logic nums[mid-1] will give wrong answer
   so we have handled it in another else
   to be desired index mid==0 and ele should be > target

3. if position is after last index 
  
   in this case simply we can return len(arr)

'''
class Solution:
    def searchInsert(self, nums, target) -> int:
        low ,high = 0, len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                return mid
            if mid!=0 and nums[mid-1]<target and nums[mid]>target:
                return mid
            elif mid == 0 and nums[mid]>target:
                return 0
            elif nums[mid]>target:
                high = mid - 1
            else:
                low = mid + 1
        return len(nums)       
        