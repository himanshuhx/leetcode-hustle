class Solution:
    def leafSimilar(self, root1, root2) -> bool:
        def dfs(root, leaves):
            if not root: return
            if not root.left and not root.right:
                leaves.append(root.val)
                
            dfs(root.left, leaves)
            dfs(root.right, leaves)
            return leaves
            
        leaf1 = dfs(root1, [])
        leaf2 = dfs(root2, [])
        return leaf1 == leaf2
        