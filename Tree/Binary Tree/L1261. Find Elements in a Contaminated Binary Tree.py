class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.val = set()
        self.dfs(root, 0)
        
    def dfs(self, root, val):
        if not root: return
        self.val.add(val)
        self.dfs(root.left, val * 2 + 1)
        self.dfs(root.right, val * 2 + 2)

    def find(self, target: int) -> bool:
        return True if target in self.val else False
