class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def dfs(i, j):
            if i >= j:
                return None
            val = preorder[i]
            root = TreeNode(val)
            idx = i+1
            while idx < j and preorder[idx] < preorder[i]:
                idx += 1
            root.left = dfs(i+1, idx)
            root.right = dfs(idx, j)

            return root

        return dfs(0, len(preorder))
