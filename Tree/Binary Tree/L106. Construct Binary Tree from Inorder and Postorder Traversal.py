class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def getIdx(val):
            for i in range(len(inorder)):
                if inorder[i] == val:
                    return i
        
        def dfs(low, high):
            if low > high:
                return None
            curr = postorder.pop()
            root = TreeNode(curr)
            mid = getIdx(curr)
            root.right = dfs(mid+1, high)
            root.left = dfs(low, mid-1)
            
            return root
        
        return dfs(0, len(postorder)-1)
        