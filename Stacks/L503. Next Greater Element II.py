class Solution:
    # vvimp
    # O(2*N) O(N) --> most optimized 
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans, stack = [], []
        for i in range(2*n-1,-1,-1):
            while stack and stack[-1]<=nums[i%n]:
                stack.pop()
            if i<n:
                if stack:
                    ans.append(stack[-1])
                else:
                    ans.append(-1)
            stack.append(nums[i%n])
        return ans[::-1]
        