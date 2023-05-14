# Naive approach
# for each node traverse whole ll and find the next greater node
# O(N^2) O(1)

# Another approach is to store values of ll in an array and do next greater element concept
# O(N) + O(N), O(N) (for array) + O(N) (for stack)

# Optimized approach is to reverse the linked list do nge
# O(N) + O(N), O(N) (for stack)
class Solution:
    def nextLargerNodes(self, head):
        nextGreater, stack = [], []
        curr = head
        prev = forw = None
        while curr:
            forw = curr.next
            curr.next = prev
            prev = curr
            curr = forw
            
        curr = prev
        while curr:
            while stack and stack[-1]<=curr.val:
                stack.pop()
            if stack:
                nextGreater.append(stack[-1])
            else:
                nextGreater.append(0)
            stack.append(curr.val)
            curr = curr.next
            
        return nextGreater[::-1]