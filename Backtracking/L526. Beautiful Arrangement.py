class Solution:
    def countArrangement(self, n: int) -> int:
        def solve(start):
            nonlocal count
            if start==n:
                count+=1
            
            for j in range(start, n):
                arr[start], arr[j] = arr[j], arr[start]
                if arr[start]%(start+1) == 0 or (start+1)%arr[start]==0:
                    solve(start+1)
                arr[start], arr[j] = arr[j], arr[start]
        
        count = 0
        arr = [i+1 for i in range(n)]
        solve(0)
        return count