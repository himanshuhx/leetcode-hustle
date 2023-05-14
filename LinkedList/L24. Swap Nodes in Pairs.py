from collections import deque
class Solution:
    def swapPairs(self, head):
        even, odd = deque(), deque()
        curr = head
        isOdd = True
        while curr:
            if isOdd:
                odd.append(curr.val)
            else:
                even.append(curr.val)
            isOdd = not isOdd
            curr = curr.next
            
        curr = head
        isOdd = True
        while curr:
            if isOdd:
                if even:
                    curr.val = even.popleft()
            else:
                if odd:
                    curr.val = odd.popleft()
            isOdd = not isOdd
            curr = curr.next
            
        return head

    
    
    def swapPairs(self, head):
        dummy = ListNode(-1, head)
        prev, curr = dummy, head
        while curr and curr.next:
            
            # save ptr
            nextPair = curr.next.next
            second = curr.next
            
            # reverse the pair
            second.next = curr
            curr.next = nextPair
            prev.next = second
            
            # update ptrs
            prev = curr
            curr = nextPair
            
        return dummy.next
            