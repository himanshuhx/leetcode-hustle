class Solution:

    # Using Stack 
    # O(N)+O(N), O(N)
    def reverseList(self, head):
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr=curr.next
        curr = head
        while curr:
            curr.val = stack.pop()
            curr = curr.next
        return head
    
'''
Remember it like this

   (start and go clockwize) 
        <---forw----
        |          |
        |          |
       curr      curr.next       
        |          ^
        |          |       
        --->prev----
'''
    # One pass O(N)

def reverseList(self, head):
        curr = head
        forw = prev = None
        while curr:
            forw = curr.next
            curr.next = prev
            prev = curr
            curr = forw
        return prev

# recursive soln
# store curr.next in forw 
# than assign prev as curr next
def reverseList(self, head):
        def solve(head, prev):
            if not head:
                return prev
            forw = head.next
            head.next = prev
            return solve(forw, head)
            
        return solve(head, None)

