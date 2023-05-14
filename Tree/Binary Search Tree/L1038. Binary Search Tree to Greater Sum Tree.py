class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root:
                return
            dfs(root.right)
            self.s += root.val
            root.val = self.s
            dfs(root.left)

        self.s = 0
        dfs(root)
        return root
