class Solution:
    def minSetSize(self, nums: List[int]) -> int:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        totalFrequency, size = 0, 0
        for frequency in sorted(count.values(), reverse=True):
            totalFrequency += frequency
            size += 1
            if totalFrequency >= len(nums)//2:
                break

        return size
