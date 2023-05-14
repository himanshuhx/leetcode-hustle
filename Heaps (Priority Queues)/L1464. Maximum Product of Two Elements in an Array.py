# time complexity --> O(N) to heapify + O((n-2)*logn) for heappop

from heapq import *


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heapify(nums)
        while len(nums) > 2:
            heappop(nums)
        return (nums[0]-1)*(nums[1]-1)
