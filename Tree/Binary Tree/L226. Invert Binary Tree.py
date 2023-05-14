class Solution:
    def invertTree(self, root):
        if not root: return        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root