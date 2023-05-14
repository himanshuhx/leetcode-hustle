class Solution:
    def flatten(self, head):
        curr = tail = head
        stack = []
        while curr:
            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                    curr.next.prev = None
                curr.next = curr.child
                curr.next.prev = curr
                curr.child = None
            tail = curr
            curr = curr.next
            
        while stack:
            node = stack.pop()
            tail.next = node
            node.prev = tail
            while node.next:
                node = node.next
            tail = node
                
        return head