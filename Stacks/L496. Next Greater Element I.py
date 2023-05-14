# made a map to get next greater element while iterating nums1 in
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextGreater = {}

        for i in range(len(nums2)-1,-1,-1):
            while stack and stack[-1]<nums2[i]:
                stack.pop()
            val = nums2[i]
            nextGreater[nums2[i]] = stack[-1] if stack else val
            stack.append(val)
        #print(nextGreater)

        for i in range(len(nums1)):
            nums1[i] = -1 if nextGreater[nums1[i]]==nums1[i] else nextGreater[nums1[i]]
        return nums1
            