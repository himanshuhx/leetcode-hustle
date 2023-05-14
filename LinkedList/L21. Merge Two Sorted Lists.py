class Solution:
    def mergeTwoLists(self, l1, l2):
        
        dummy = head = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        dummy.next = l1 or l2
        return head.next
                
            
        