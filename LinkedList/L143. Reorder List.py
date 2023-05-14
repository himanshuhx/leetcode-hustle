import collections
class Solution:
    def reorderList(self, head):
        stack, queue = [], collections.deque()
        
        # find mid of ll 
        slow = fast = head
        while fast and fast.next:
            queue.append(slow.val)
            slow = slow.next
            fast = fast.next.next            
            
        while slow:
            stack.append(slow.val)
            slow = slow.next
            
        curr, isOdd = head, True
        while curr:
            if isOdd and queue:
                curr.val = queue.popleft()
            else:
                curr.val = stack.pop()
            isOdd = not isOdd
            curr = curr.next
        return head
            
# O(1)
    def reorderList(self, head) -> None:
        def merge(l1, l2):
            while l2:
                next1 = l1.next
                l1.next = l2
                l1=l2
                l2=next1
            
            
        def reverseTheLinkedList(head):
            curr, forw, prev = head, None, None
            while curr:
                forw = curr.next
                curr.next = prev
                prev = curr
                curr = forw
            return prev
        
        slow = fast = prev =head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        l1 = head
        prev.next = None
        l2 = reverseTheLinkedList(slow)
        
        merge(l1, l2)            
            
        
            
        