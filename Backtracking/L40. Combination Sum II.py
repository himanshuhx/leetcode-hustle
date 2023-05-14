class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def solve(start, target, curr):
            if target==0:
                ans.append(curr[:])
                return
            for j in range(start, n):
                if j>start and candidates[j]==candidates[j-1]:
                    continue
                if candidates[j]<=target:
                    curr.append(candidates[j])
                    solve(j+1, target-candidates[j], curr)
                    curr.pop()
        
        ans, n = [], len(candidates)
        candidates.sort()
        solve(0, target, [])
        return ans