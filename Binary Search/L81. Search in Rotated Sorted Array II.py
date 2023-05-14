class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums)-1
        while low<=high:
            mid = low + (high-low)//2
            if nums[mid]==target:
                return True
            while low<mid and nums[low]==nums[mid]: # tricky part (to remove duplicates)
                low+=1
            if nums[low]<=nums[mid]:
                if target>=nums[low] and target<=nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if target>=nums[mid] and target<=nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False