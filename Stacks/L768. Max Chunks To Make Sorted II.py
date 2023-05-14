# https://leetcode.com/problems/max-chunks-to-make-sorted-ii/discuss/595713/Monotonic-stack-solution-with-detailed-explanation

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for i in range(len(arr)):
            largest = arr[i]
            while stack and stack[-1]>arr[i]:
                largest = max(largest, stack.pop())
            stack.append(largest)
            
        return len(stack)