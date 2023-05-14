from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        queue, leftSum = deque(), 0
        queue.append(root)
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    if not node.left.left and not node.left.right:
                        leftSum += node.left.val
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return leftSum