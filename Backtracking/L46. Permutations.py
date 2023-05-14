# https://www.youtube.com/watch?v=GuTPwotSdYw


# if [size of all outputs are same] as that of input it is a case of [permutation]
# else there is a certain variable given (k) and [outputs are of length k]
# its [combination] idea

from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def solve(i):
            if i==len(nums):
                ans.append(nums[:])
                return
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                solve(i+1)
                nums[i], nums[j] = nums[j], nums[i]
        
        ans = []
        solve(0)
        return ans