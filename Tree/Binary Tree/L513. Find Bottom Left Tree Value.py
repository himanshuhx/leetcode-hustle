from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)
        bottom_left = 0
        while queue:
            bottom_left = queue[0].val
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return bottom_left