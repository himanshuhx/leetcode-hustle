class Solution:
    def oddEvenList(self, head):
        odd = oddHead = ListNode(0)
        even = evenHead = ListNode(0)
        isOdd = True
        
        while head:
            if isOdd:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            isOdd = not isOdd
            head = head.next
            
        even.next = None
        odd.next = evenHead.next
        return oddHead.next