
class Solution:
    # naive approach is for every node in 2 ll we find is there a same node in ll 1
    # O(N*M) O(1)

    # Set Approach
    # O(N+M) O(N)
    def getIntersectionNode(self, headA, headB):
        s=set()
        while headA:
            s.add(headA)
            headA=headA.next
        while headB:
            if headB in s:
                return headB
            headB=headB.next
        return None

    # Optimized Approach
    # O(2*M), O(1)
    def getIntersectionNode(self, headA, headB):
        a = headA
        b = headB
        while a!=b:
            a = headB if not a else a.next
            b = headA if not b else b.next
        return a