class Solution:
    def splitListToParts(self, head, k):
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        q, r = divmod(length, k)
        
        ans, curr = [], head
        
        for i in range(k):
            size = q + 1 if r>0 else q
            r-=1
            ans.append(curr)
            
            prev = None
            while size:
                prev = curr
                curr = curr.next
                size -= 1
                
            if prev: prev.next = None
                
        return ans