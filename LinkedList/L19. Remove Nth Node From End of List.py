class Solution:
    def removeNthFromEnd(self, head, n: int):
        curr = head
        size = 0
        while curr:
            size += 1
            curr = curr.next        
        
        if size == n:
            return head.next
        
        curr = head
        for i in range(size-n-1):
            curr = curr.next
            
        curr.next = curr.next.next
        return head


    # O(N), O(1)
    def removeNthFromEnd(self, head, n: int):
        slow = fast = dummy = ListNode(-1)
        dummy.next = head
        
        for i in range(n):
            fast = fast.next
            
        while fast.next:
            slow = slow.next
            fast = fast.next
            
        slow.next = slow.next.next
        
        return dummy.next
        