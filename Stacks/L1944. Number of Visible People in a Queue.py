class Solution:

    ## vimp next greater element advanced amazon
    def canSeePersonsCount(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return [0]
        stack, ans = [], []
        
        for i in range(len(nums)-1,-1,-1):
            count = 0
            while stack and stack[-1]<=nums[i]:
                count+=1
                stack.pop()
            if stack:
                count += 1
            ans.append(count)
            stack.append(nums[i])
            
        return ans[::-1]
            