class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def solve(start, count, target, curr):
            if target==0 and count==0:
                ans.append(curr[:])
            if target==0 or count==0:
                return
            for j in range(start, 9):
                if target>=arr[j] and arr[j] not in visited:
                    curr.append(arr[j])
                    visited.add(arr[j])
                    solve(j+1, count-1, target-arr[j], curr)
                    curr.pop()
                    visited.remove(arr[j])
        
        arr = [i+1 for i in range(9)]
        ans = []
        visited = set()
        solve(0, k, n, [])
        return ans