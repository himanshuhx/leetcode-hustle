class Solution:
    # naive approach for each node check whether tree is balanced or not o(n^2)

    # o(n) approach
    def isBalanced(self, root) -> bool:
        def dfs(root):
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if abs(left-right)>1: self.bal = False
            return 1 + max(left,right)
        
        self.bal = True
        dfs(root)
        return self.bal