from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(root)
        isEnd = False
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if not node: isEnd = True
                else:
                    if isEnd:
                        return False
                    queue.append(node.left)
                    queue.append(node.right)
                    
        return True