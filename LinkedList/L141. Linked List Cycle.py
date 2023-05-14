class Solution:

    # O(N) O(N) using set
    def hasCycle(self, head) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False
    
    # slow and fast pointer O(N) O(1)
    def hasCycle(self, head) -> bool:
        slow = fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                return True
        return False