'''
Algorithm ( O(N)+O(N), O(N) )

1. initialize a hashmap
2. iterate and add original linked list node as key and create a new Listnode with value
as that of original node. (No ptrs oper. will be done here)
3. Now do the pointer part.
   how we will get next and random? --> key in map is original node from there
   what if next or random is none??
   --> for that initialize a special None:None mapping in map. 

'''

class Solution:
    def copyRandomList(self, head):
        oldToCopy = { None : None }
        
        curr = head
        while curr:
            oldToCopy[curr] = ListNode(curr.val)
            curr = curr.next
            
        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next
            
        return oldToCopy[head]