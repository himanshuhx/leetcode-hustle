'''
vvvimp points for sliding window questions

in questions of sliding window where it states to find a window with k unique characters
==> find slidingWindow(k)-slidingWindow(k-1) to get exact k unique characters window
no of subarrays 

==> ans += j-i+1 (no need to check whether window Size==k or not in each iteration add
because every time j increments a new subarray is formed and since we are eliminating invalid window
in 2nd while loop before coming to this part hence we know our current subarray is also valid)

'''
import collections
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.slidingWindow(nums,k)-self.slidingWindow(nums,k-1)
    
    def slidingWindow(self,nums,k):
        i, j = 0, 0
        ans = 0
        count = collections.defaultdict(int)
        while j<len(nums):
            count[nums[j]]+=1
            while len(count)>k:
                count[nums[i]]-=1
                if count[nums[i]]==0:
                    count.pop(nums[i])
                i+=1
            ans += j-i+1
            j+=1
        return ans