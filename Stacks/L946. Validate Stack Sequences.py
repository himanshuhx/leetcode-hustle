# O(N) O(N)
# https://www.youtube.com/watch?v=SeTsK_aNUWI

from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        for x in pushed:
            stack.append(x)
            while stack and stack[-1]==popped[j]:
                stack.pop()
                j+=1
        return j==len(popped)