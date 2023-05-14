from collections import Counter
from heapq import *


class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        maxheap = []
        for ch, freq in count.items():
            heappush(maxheap, (-freq, ch))

        ans = ""
        prev_char_freq, prev_char = 0, ''

        while maxheap:
            current_char_freq, current_char = heappop(maxheap)
            ans += current_char

            if prev_char_freq < 0:
                heappush(maxheap, (prev_char_freq, prev_char))

            current_char_freq += 1
            prev_char_freq, prev_char = current_char_freq, current_char

        return ans if len(ans) == len(s) else ""
