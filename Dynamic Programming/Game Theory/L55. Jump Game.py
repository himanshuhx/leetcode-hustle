## vvimp

# vvvvvimp
class Solution:

    #0n^2 0n
    def canJump(self, nums: List[int]) -> bool:
        def solve(i):
            if i==n-1:
                return True
            if i>=n:
                return False
            if nums[i]==0:
                return False 
            
            for j in range(1,nums[i]+1):
                if solve(i+j):
                    return True
            return False
        
        n = len(nums)
        return solve(0)

    # 0n 01
    def canJump(self, nums: List[int]) -> bool:
        maxi = 0
        for i in range(len(nums)):
            if i>maxi:
                return False
            maxi = max(maxi,i+nums[i])
        return True
            