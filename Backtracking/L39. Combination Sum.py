class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def solve(start, target, curr):
            if target==0:
                ans.append(curr[:])
                return 
            if start==n or target<0:
                return
            if candidates[start]<=target:
                curr.append(candidates[start])
                solve(start, target-candidates[start], curr)
                curr.pop()
            solve(start+1, target, curr)
        
        ans, n = [], len(candidates)
        solve(0, target, [])
        return ans
        