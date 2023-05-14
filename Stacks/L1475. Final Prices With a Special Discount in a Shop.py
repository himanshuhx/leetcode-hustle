class Solution:
    def finalPrices(self, nums: List[int]) -> List[int]:
        stack = []
        ans = []
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[i]<stack[-1]:
                stack.pop()
            if stack:
                ans.append(nums[i]-stack[-1])
            else:
                ans.append(nums[i])
            stack.append(nums[i])
        return ans[::-1]

    # in place modification without ans
    def finalPrices(self, nums: List[int]) -> List[int]:
        stack = []
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[i]<stack[-1]:
                stack.pop()
            val = nums[i]
            if stack:
                nums[i]-=stack[-1]
            stack.append(val)
        return nums