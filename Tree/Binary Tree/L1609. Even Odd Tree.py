from collections import deque
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)
        is_odd = True
        while q:            
            prev = None
            for i in range(len(q)):
                node = q.popleft()
                if is_odd:
                    if not node.val%2: return False
                    if prev and prev.val>=node.val: return False
                else:
                    if node.val%2: return False
                    if prev and prev.val <= node.val: return False               
                if node.left: 
                    q.append(node.left)
                if node.right:
                    q.append(node.right) 
                prev = node
            is_odd = not is_odd
        return True