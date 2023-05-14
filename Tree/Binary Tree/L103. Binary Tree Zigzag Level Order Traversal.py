from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return
        queue = deque()
        queue.append(root)
        is_odd = True
        zigzag = []
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                level.append(node.val)
            if is_odd: zigzag.append(level)
            else: zigzag.append(level[::-1])
            is_odd = not is_odd
        return zigzag