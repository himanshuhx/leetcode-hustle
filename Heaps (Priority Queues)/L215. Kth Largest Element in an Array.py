# very important question

from heapq import *


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)
        return heap[0]

# quickSelect O(N)
# https://www.youtube.com/watch?v=XEmy13g1Qxc
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1

            nums[p], nums[r] = nums[r], nums[p]
            if p > k:
                return quickSelect(l, p-1)
            elif p < k:
                return quickSelect(p+1, r)
            else:
                return nums[p]

        k = len(nums) - k
        return quickSelect(0, len(nums)-1)
