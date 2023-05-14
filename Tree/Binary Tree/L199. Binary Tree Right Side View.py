from collections import deque
class Solution:
    # O(N), O(width of binary tree)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return
        queue, ans = deque(), []
        queue.append(root)
        while queue:
            ans.append(queue[-1].val)
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return ans

    # O(N), O(H) (i skewed ~ O(N))
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, level):
            if not root: return
            if level == len(self.ans):
                self.ans.append(root.val)
            dfs(root.right, level+1)
            dfs(root.left, level+1)
            
        self.ans = []
        dfs(root, 0)
        return self.ans