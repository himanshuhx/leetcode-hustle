from heapq import *
from collections import Counter


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        count = Counter(barcodes)
        maxheap = []
        for ch, freq in count.items():
            heappush(maxheap, (-freq, ch))

        ans = []
        prev_code_freq, prev_code = 0, None
        while maxheap:
            curr_code_freq, curr_code = heappop(maxheap)
            ans.append(curr_code)

            if prev_code_freq < 0:
                heappush(maxheap, (prev_code_freq, prev_code))

            curr_code_freq += 1
            prev_code_freq, prev_code = curr_code_freq, curr_code

        return ans
