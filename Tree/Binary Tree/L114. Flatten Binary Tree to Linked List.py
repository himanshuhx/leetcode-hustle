from collections import deque

# time complexity - O(N) + O(N) , space complexity - O(N)
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def dfs(root):
            if not root: return
            queue.append(root)
            dfs(root.left)
            dfs(root.right)
        
        if root:
            head = root
            queue = deque()
            dfs(root)
            queue.popleft()
            while queue:
                node = queue.popleft()
                root.left = None
                root.right = node
                root = root.right


# reverse preorder traversal optimized approach
class Solution:
    def __init__(self):
        self.prev = None
        
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root: return
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root
            
        