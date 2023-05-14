from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def solve(start, curr, k):
            if k == 0:
                ans.append(curr[:])
                return
            if start == n:
                return
            for j in range(start, n):
                curr.append(arr[j])
                solve(j+1, curr, k-1)
                curr.pop()
        
        ans = []
        arr = [i+1 for i in range(n)]
        solve(0, [], k)
        return ans