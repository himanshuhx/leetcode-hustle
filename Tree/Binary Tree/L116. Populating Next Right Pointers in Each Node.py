from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return
        q = deque()
        q.append(root)
        
        while q:
            curr_len = len(q)
            for i in range(curr_len):
                node = q.popleft()
                if i == curr_len - 1:
                    node.next = None
                else:
                    node.next = q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
        return root

# O(N), O(1)
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return
        
        start = curr = root
        while curr.left:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
                curr = curr.next
            else:
                curr.next = None
                curr = start.left
                start = curr
                
        return root