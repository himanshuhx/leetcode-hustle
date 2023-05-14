# Approach 1 use two stacks 

# approach 2 by reversing the linked list
class Solution:
    def addTwoNumbers(self, l1, l2):
        def reverseTheLinkedList(head):
            curr = head
            forw = prev = None
            while curr:
                forw = curr.next
                curr.next = prev
                prev = curr
                curr = forw
            return prev
        
        l1 = reverseTheLinkedList(l1)
        l2 = reverseTheLinkedList(l2)
        
        dummy = head = ListNode(0)
        carry = 0
        
        while l1 or l2 or carry:
            num = 0
            if l1: num += l1.val
            if l2: num += l2.val
            num += carry
            
            dummy.next = ListNode(num % 10)
            dummy = dummy.next
            
            carry = num // 10
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        head = reverseTheLinkedList(head.next)
        return head