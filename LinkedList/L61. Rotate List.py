'''
Naive approach --> traverse list for k times and each time remove last node and add it in front
O(N*K), O(1)
'''
# store value in arr split arr from idx position and join back
# copy values back
# O(N)+O(N)+O(N), O(N)
class Solution:
    def rotateRight(self, head, k):
        if not head:
            return
        
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
            
        k = k % len(values)
        idx = len(values)-k
        
        values = values[idx:] + values[:idx]
        
        curr = head
        for value in values:
            curr.val = value
            curr = curr.next
            
        return head

    # Optimal Approach
    # O(N) + O(size - (size%k)), O(1)
    # https://www.youtube.com/watch?v=9VPm6nEbVPA&t=576s
    def rotateRight(self, head, k):
        if not head:
            return
        
        curr, prev, size = head, None, 0
        while curr:
            size += 1
            prev = curr
            curr = curr.next
        
        k = k % size
        prev.next = head # making the list circular by poiniting last node to head
        noOfTimesToIterateFromStart = size - k

        curr, newHead, prev = head, None, None
        for i in range(noOfTimesToIterateFromStart):
            prev = curr
            curr = curr.next
        newHead = prev.next
        prev.next = None
        
        return newHead