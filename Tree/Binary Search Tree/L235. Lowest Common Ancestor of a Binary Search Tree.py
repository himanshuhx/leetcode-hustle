class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def dfs(root):
            if root.val > p.val and root.val > q.val: return dfs(root.left)
            elif root.val < p.val and root.val < q.val: return dfs(root.right)
            else: return root        
        
        return dfs(root)