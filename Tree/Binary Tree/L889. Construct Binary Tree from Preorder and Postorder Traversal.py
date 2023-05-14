# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/discuss/1615841/python3-both-on2-and-on-solution
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def findRootOfLeftSubTreeInPostorderArray(num):
            for i in range(len(postorder)):
                if postorder[i] == num:
                    return i
        
        def dfs(preStart, preEnd, postStart, postEnd):
            if preStart>preEnd: return None
            root = TreeNode(preorder[preStart])            
            if preStart == preEnd: return root
            
            idx = findRootOfLeftSubTreeInPostorderArray(preorder[preStart+1])
            l = idx - postStart + 1
            root.left = dfs(preStart+1, preStart+l, postStart, idx)
            root.right = dfs(preStart+l+1, preEnd, idx+1, postEnd)
            
            return root
               
        return dfs(0, len(preorder)-1, 0, len(postorder)-1)


    # optimized above O(n^2) to O(N) using extra space
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def dfs(preStart, preEnd, postStart, postEnd):
            if preStart>preEnd: return None
            root = TreeNode(preorder[preStart])            
            if preStart == preEnd: return root
            
            idx = postorderMap[preorder[preStart+1]]
            l = idx - postStart + 1
            root.left = dfs(preStart+1, preStart+l, postStart, idx)
            root.right = dfs(preStart+l+1, preEnd, idx+1, postEnd)
            
            return root
        
        postorderMap = {}
        for i, value in enumerate(postorder):
            postorderMap[value] = i
            
        return dfs(0, len(preorder)-1, 0, len(postorder)-1)