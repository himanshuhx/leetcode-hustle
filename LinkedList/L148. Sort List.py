class Solution:

    # store in arr -> sort arr --> copy values
    # O(N) + O(NlogN) + O(N), O(N)
    def sortList(self, head):
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        
        curr = head
        values.sort()
        for value in values:
            curr.val = value
            curr = curr.next
            
        return head

# O(nlogn), O(logn) 
# recursive tree --> logn (for splitting into two halves)
# logn for merging and each operation takes O(n) (mergeList func call)
# so n(logn)
# logn space for call stack
class Solution:
    # code same as find middle of linked list L876
    def getMid(self, head):
        slow , fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    # code same as merge two sorted lists L21
    def mergeList(self, list1, list2):
        tail = dummy = ListNode(-1)
        
        while list1 and list2:
            if list1.val<list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            
        tail.next = list1 or list2
        
        return dummy.next
            
    def sortList(self, head):
        if not head or not head.next:
            return head
        
        # split the linked list into two halfs
        left = head
        right = self.getMid(left)
        temp = right.next
        right.next = None
        right = temp
        
        left = self.sortList(left)
        right = self.sortList(right)
        
        return self.mergeList(left,right)    