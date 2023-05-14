'''
sort the smaller array
iterate the larger array and perform binary search
Time complexity - O(larger array size)*log(smaller array size)

'''
class Solution:
    def binarySearch(self, arr, target):
        low, high = 0, len(arr)-1
        while low<=high:
            mid = (low+high)//2
            if arr[mid]==target:
                return True
            elif arr[mid]>target:
                high = mid-1         
            else:
                low = mid+1
        return False
    
    def intersection(self, nums1, nums2):
        if len(nums1)>len(nums2):
            nums2, nums1 = nums1, nums2
        nums1.sort()
        ans = set()
        for num in nums2:
            if num not in ans and self.binarySearch(nums1,num):
                ans.add(num)
        return ans
        