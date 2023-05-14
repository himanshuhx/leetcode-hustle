from heapq import *


class Solution:

    # time complexity - O(n) + O(nlogn) + O(k), space complexity - O(N)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        ans = []
        freq = sorted(freq.items(), key=lambda a: a[1], reverse=True)

        for i in range(k):
            ans.append(freq[i][0])

        return ans

 # time complexity - O(n) + O(nlogk) + O(k), space complexity - O(N+K)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        heap = []
        for num, count in freq.items():
            if len(heap) < k:
                heappush(heap, (count, num))
            else:
                heappushpop(heap, (count, num))

        ans = []
        for ele in heap:
            ans.append(ele[1])

        return ans

# bucket sort   time complexity - O(n) + O(n) + O(k), space complexity - O(N+N)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        bucket = [[] for i in range(len(nums)+1)]

        for num, count in freq.items():
            bucket[count].append(num)

        ans = []
        for i in range(len(bucket)-1, -1, -1):
            if len(ans) >= k:
                return ans[:k+1]
            if bucket[i]:
                ans += bucket[i]

        return ans
