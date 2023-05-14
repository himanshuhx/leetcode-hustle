'''
Some IMPORTANT POINTS

if we want kth smallest element
--> we need maximum heap and insert element with -ve sign
--> for pop operation the incoming number should be greater than top element of heap



SOme approaches to this question ---

1. custom based sorting - nlogn
2. heap approach but heapify whole array -- extra space taken will be O(n) we can reduce it
to k in 3 approach
3. maintain a heap of size k instead of heapifying whole array.
'''

# Time complexity - nlog k
from heapq import *


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            distance = x**2 + y**2
            if len(heap) < k:
                heappush(heap, (-distance, [x, y]))
            else:
                if -distance > heap[0][0]:
                    heappop(heap)
                    heappush(heap, (-distance, [x, y]))
        ans = []
        for i in range(k):
            ans.append(heap[i][1])
        return ans
