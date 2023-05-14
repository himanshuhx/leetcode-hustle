class Solution:
    def nodesBetweenCriticalPoints(self, head):
        i =  0
        curr, prev = head, None
        minimum_critical_distance = float("inf")
        prev_critical_point = first_critical_point = None
        
        while curr:
            i += 1            
            # check for maxima and minima
            if prev and curr.next:
                if (prev.val<curr.val and curr.val>curr.next.val) or (prev.val>curr.val and curr.val<curr.next.val):
                    
                    if not first_critical_point:
                        first_critical_point = i
                        
                    if prev_critical_point:
                        minimum_critical_distance = min(minimum_critical_distance, i - prev_critical_point)
                        
                    prev_critical_point = i
                    
            prev = curr
            curr = curr.next
        
        # if no min distance found
        if minimum_critical_distance == float("inf"):
            return [-1,-1]

        return [minimum_critical_distance, prev_critical_point - first_critical_point]  