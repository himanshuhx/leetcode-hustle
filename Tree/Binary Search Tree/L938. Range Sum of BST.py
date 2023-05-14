# level order O(N), O(N)
from collections import deque
class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        q, ans = deque(), 0
        q.append(root)        
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.val >= low and node.val <= high: ans += node.val
                if node.right: q.append(node.right)
                if node.left: q.append(node.left)
        return ans