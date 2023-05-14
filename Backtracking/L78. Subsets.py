class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def solve(i, curr):
            ans.append(curr[:])
            for j in range(i,len(nums)):
                curr.append(nums[j])
                solve(j+1,curr)
                curr.pop()
            
        ans = []
        solve(0, [])
        return ans