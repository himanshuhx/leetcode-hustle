class Solution:
    def removeZeroSumSublists(self, head):
        dummy = ListNode(0)
        seen, prefixSum = { 0 : dummy }, 0
        dummy.next = curr = head
        
        while curr:
            prefixSum += curr.val
            seen[prefixSum] = curr
            curr = curr.next
            
        curr, prefixSum = dummy, 0
        while curr:
            prefixSum += curr.val
            curr.next = seen[prefixSum].next
            curr = curr.next
            
        return dummy.next