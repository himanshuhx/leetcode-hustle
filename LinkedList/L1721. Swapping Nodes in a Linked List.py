class Solution:

    # O(N)+O(N) two pass soln, O(1)
    # find length find node from start and end swap the values
    def swapNodes(self, head, k):
        kStart = kEnd = None
        curr = head
        l = 0
        while curr:
            l+=1
            curr = curr.next
        
        curr = head
        for i in range(l):
            if i == k-1:
                kStart = curr
            if i == l-k:
                kEnd = curr
            curr = curr.next
        
        
        # swap the values
        kStart.val, kEnd.val = kEnd.val, kStart.val
        return head

    # O(N), O(1)
    # fast and slow pointers
    def swapNodes(self, head, k):
        slow = fast = head
        for i in range(1, k):
            slow = slow.next
            
        curr = slow
        while curr.next:
            fast = fast.next
            curr = curr.next
            
        slow.val, fast.val = fast.val, slow.val
        return head