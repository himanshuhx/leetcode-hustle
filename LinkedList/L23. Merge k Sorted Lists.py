# O(N*K) O(1) soln
# used merge two linked list algo to merge all k lists taken two at a time

class Solution:
    def mergeKLists(self, lists):
        if not lists: return
        
        def mergeTwoList(l1, l2):
            ans = dummy = ListNode(-1)
            
            while l1 and l2:
                if l1.val < l2.val:
                    dummy.next = l1
                    dummy = dummy.next
                    l1 = l1.next
                else:
                    dummy.next = l2
                    dummy = dummy.next
                    l2 = l2.next
                    
            dummy.next = l1 or l2
            return ans.next
        
        res = lists[0]
        for i in range(1, len(lists)):
            res = mergeTwoList(res, lists[i])
            
        return res