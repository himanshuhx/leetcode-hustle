# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        if not head:
            return head.val
        
        curr = head
        size = 0
        while curr:
            size+=1
            curr = curr.next

        size -= 1    
        num = 0
        curr = head
        while curr:
            num = num + curr.val * (2**size)
            size-=1
            curr = curr.next
            
        return num