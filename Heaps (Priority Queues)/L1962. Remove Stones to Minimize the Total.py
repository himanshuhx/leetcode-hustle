from heapq import *


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-pile for pile in piles]
        heapify(heap)
        for i in range(k):
            x = heappop(heap)
            heappush(heap, floor(x//2))

        res = 0
        for e in heap:
            res += -e

        return res
