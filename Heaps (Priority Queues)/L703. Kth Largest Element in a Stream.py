from heapq import *


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapify(self.heap)
        while len(self.heap) > k:
            heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        else:
            heappushpop(self.heap, val)

        return self.heap[0]
