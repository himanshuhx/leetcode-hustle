class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def solve(i, currXor):
            if i>=len(nums):
                return currXor
            included = solve(i+1, currXor^nums[i])
            excluded = solve(i+1, currXor)
            return included + excluded
        
        return solve(0,0)