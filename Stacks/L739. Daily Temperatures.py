class Solution:
    # brute force can be done in O(N^2)

    # O(N) O(N)
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        stack, ans = [],[0]*len(nums)
        n = len(nums)
        for i in range(n-1,-1,-1):
            while stack and nums[i]>=nums[stack[-1]]:
                stack.pop()
            if stack:
                ans[i]=stack[-1]-i
            stack.append(i)
        return ans
    
    # O(N) O(1)  vvimp (next greater how to do without extra space)
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        n = len(nums)
        hottest, curr = 0, 0
        for i in range(n-1,-1,-1):
            curr = nums[i]
            if hottest<=curr: # if curr index temp is highest of the temp we seen so far
                hottest = curr
            else: # if there is a higher temp to right which we seen earlier
                j=1
                while j<n and nums[i]>=nums[i+j]: # go from i+1 to n till we found a temp
                    j += ans[i+j]  # which is higher than our curr temp 
                    # why i+j? because ans[k] represents how much day from curr day
                    # is our next hotter element so we can skip indexes efficiently
                    # which have tempretures lower than our curr index 
                ans[i] = j # at j days from i we will get next hotter day
        return ans