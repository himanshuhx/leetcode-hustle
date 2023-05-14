
from collections import deque, Counter
from heapq import *


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        q = deque()
        time = 0

        max_heap = [-cnt for cnt in count.values()]
        heapify(max_heap)

        while max_heap or q:
            time += 1
            if max_heap:
                cnt = 1 + heappop(max_heap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heappush(max_heap, q.popleft()[0])

        return time
