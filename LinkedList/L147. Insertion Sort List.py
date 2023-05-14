'''
Idea is to create a dummy reference for our ans

ans = ListNode(-1)

1. run a loop while linked list is not null
2. pick 1st element of unsorted linked list break each link make its next to null
3. call the function and insert it at correct position
4. making dummy node gives an advantage over the edge case where 1st element of sorted list 
is greater than toPlace element for ex - ans-->5  node toplace = 4

'''

# there is a constant space optimal soln O(1) watch it
class Solution:
    def insertionSortList(self, head):
        def insertAtCorrectPlace(toPlace):
            if not ans.next:  # if our ans LL is empty
                ans.next = toPlace
                return
            
            ansHead = ans.next
            prev, curr = ans, ansHead             
            while curr:
                if curr.val > toPlace.val:
                    prev.next = toPlace
                    toPlace.next = curr
                    return
                prev = curr
                curr = curr.next
                
            prev.next = toPlace # if we reached the end of LL and didn't found the place. e.g ans->2->3->4 node to be inserted = 5
                                            # in this case since curr would have become null but we have prev pointer. 
        ans = ListNode(-1)
        curr = head
        while curr:
            nextt = curr.next # save our next ptr
            curr.next = None 
            insertAtCorrectPlace(curr)
            curr = nextt
            
        return ans.next