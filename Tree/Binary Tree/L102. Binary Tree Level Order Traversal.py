from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return
        queue = deque()
        queue.append(root)
        ans = []
        while queue:
            level = []
            for i in range(len(queue)):
                
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
                level.append(node.val)
            ans.append(level)
        return ans