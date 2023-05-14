class Solution:

    # this recursion pattern template can be used for ques like deepest leaves, ancestors
    
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root: return None, 0
            leftNode, left = dfs(root.left)
            rightNode, right = dfs(root.right)
            if left>right:
                return leftNode, 1+left
            elif right>left:
                return rightNode, 1+right
            else:
                return root, 1+left
            
        node, depth = dfs(root)
        return node