from heapq import *


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = collections.Counter(words)
        ans = []
        for word in sorted(freq.items(), key=lambda a: (-a[1], a[0])):
            if len(ans) == k:
                return ans
            ans.append(word[0])

        return ans


class ArrangeAccToFreqElseLexi:

    def __init__(self, count, word):
        self.count = count
        self.word = word

    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = collections.Counter(words)
        heap = []
        for word, count in freq.items():
            heappush(heap, ArrangeAccToFreqElseLexi(count, word))
            if len(heap) > k:
                heappop(heap)

        return [heappop(heap).word for i in range(k)][::-1]
