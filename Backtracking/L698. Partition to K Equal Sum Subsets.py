# Time complexity 0(2^(k*n))

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:             
        if sum(nums)%k:
            return False
        used = [False] * len(nums)
        target = sum(nums)//k
        
        def dfs(i, k, currSum):
            if k==0:
                return True
            if target==currSum:
                return dfs(0, k-1, 0)
                
            for j in range(i, len(nums)):
                if not used[j] and nums[j]+currSum<=target:
                    used[j] = True
                    if dfs(j+1, k, nums[j]+currSum):
                        return True
                    used[j] = False
            return False

        return dfs(0, k, 0)
        