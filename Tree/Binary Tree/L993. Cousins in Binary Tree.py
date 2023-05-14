class Solution:
    def isCousins(self, root, x: int, y: int) -> bool:
        def dfs(root, parent, depth):
            nonlocal d1, p1, d2, p2
            if not root: return
            dfs(root.left, root, depth+1)
            if root.val == x:
                d1, p1 = depth, parent.val
            if root.val == y:
                d2, p2 = depth, parent.val
            dfs(root.right, root, depth+1)
            
            
        d1, p1, d2, p2 = -1, None, -2, None 
        dfs(root, TreeNode(-1), 0)
        return d1==d2 and p1 != p2