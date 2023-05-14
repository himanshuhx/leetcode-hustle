class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(root, parent, grandparent):
            if not root: return
            dfs(root.left, root, parent)
            if grandparent and grandparent.val % 2 == 0:
                self.ans += root.val
            dfs(root.right, root, parent)
        
        
        self.ans = 0
        dfs(root, None, None)
        return self.ans
        