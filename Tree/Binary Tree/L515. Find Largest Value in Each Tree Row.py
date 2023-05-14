from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return
        q = deque()
        q.append(root)
        largest_value_in_each_row = []
        while q:
            lar = -float("inf")
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                lar = max(lar, node.val)
            largest_value_in_each_row.append(lar)
        return largest_value_in_each_row