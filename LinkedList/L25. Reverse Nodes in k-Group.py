class Solution:
    def reverseKGroup(self, head, k):
        def reverseTheList(head_):
            curr, prev, forw = head_, None, None
            for i in range(k):
                forw = curr.next
                curr.next = prev
                prev = curr
                curr = forw
            return (prev, forw)
        
        if not head or k==1: return head
        curr, size = head, 0
        while curr:
            size += 1
            curr = curr.next
        
        dummy = prev = ListNode(-1)
        dummy.next = head
        curr = head
        while size >= k:
            tailAfterReversing = curr
            prev.next, curr = reverseTheList(curr)
            prev = tailAfterReversing
            size -= k
        if curr:
            prev.next = curr
        return dummy.next
            
        
        