class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def dfs(root):
            if not root: return
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            if root.val in toDelete:
                if root.left: self.forest.append(root.left)
                if root.right: self.forest.append(root.right)
                return None
            return root
        
        toDelete = set(to_delete)
        self.forest = []
        dfs(root)
        if not root.val in toDelete:
            self.forest.append(root)
        return self.forest