class Solution:
    # Two pass 
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length+=1
            curr = curr.next
        length = length//2
        curr = head
        while length:
            curr = curr.next
            length-=1
            
        return curr

    # hair and tortoise method (One pass)
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow