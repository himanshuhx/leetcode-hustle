class Solution:

    # N^3-->N^2-->N
    # https://www.youtube.com/watch?v=xV-QDXn9Brc
    # amazon vvimp
    def find132pattern(self, nums: List[int]) -> bool:
        min_list, stack = [], []
        min_list.append(nums[0])
        for i in range(1,len(nums)):
            min_list.append(min(min_list[-1],nums[i]))
        for i in range(len(nums)-1,-1,-1):
            while stack and min_list[i]>=stack[-1]:
                stack.pop()               
            if stack and nums[i]>stack[-1]:
                return True
            stack.append(nums[i])
        return False