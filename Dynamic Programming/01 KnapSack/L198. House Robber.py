class Solution:
    def rob(nums):

        def solveM(idx):
            if idx<0:
                return 0
            if memo[idx]!=-1:
                return memo[idx]
            memo[idx] = max(nums[idx]+solveM(idx-2),solveM(idx-1))
            return memo[idx]

        def solveR(idx):
            if idx<0:
                return 0
            return max(nums[idx]+solveR(idx-2),solveR(idx-1))

            
        n=len(nums)
        memo = [-1]*n
        return solveM(n-1)