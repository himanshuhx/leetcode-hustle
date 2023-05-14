class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def getIdx(val):
            for i in range(len(inorder)):
                if inorder[i] == val:
                    return i
        
        def dfs(ps, pe, ins, ine):
            if ps > pe: return None
            curr = preorder[ps]
            root = TreeNode(curr)
            if ps == pe:
                return root
            
            idx = getIdx(curr)

            root.left = dfs(ps + 1, ps + idx - ins, ins, idx - 1)
            root.right = dfs( pe - ine + idx + 1, pe, idx + 1, ine)
            return root
        
        return dfs(0, len(preorder)-1, 0, len(inorder)-1)