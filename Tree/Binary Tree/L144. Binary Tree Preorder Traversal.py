class Solution:

    # recursive implementation O(N), O(N)
    def preorderTraversal(self, root):
        def dfs(root):
            if not root: return
            pre.append(root.val)
            dfs(root.left)
            dfs(root.right)
            
        pre = []
        dfs(root)
        return pre

    # iterative implementation O(N), O(N)
    def preorderTraversal(self, root):
        stack, pre = [], []
        curr = root
        while curr or stack:            
            while curr:
                pre.append(curr.val)
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()           
            curr = curr.right
        return pre         

    # Morris Traversal O(N), O(1)
    def preorderTraversal(self, root):
        pre = []
        
        curr = root
        while curr:
            # if there is no left print curr and move to right
            if not curr.left:
                pre.append(curr.val)
                curr = curr.right
                
            # if there is left
            else:
                
                rightMostOfLeftSubTree = prev = curr.left
                while rightMostOfLeftSubTree and rightMostOfLeftSubTree.right != curr:
                    prev = rightMostOfLeftSubTree
                    rightMostOfLeftSubTree = rightMostOfLeftSubTree.right
                
                # if there is no cycle and we didnt marked the right to curr ever
                if not rightMostOfLeftSubTree:
                    prev.right = curr
                    pre.append(curr.val)
                    curr = curr.left
                # if we have marked it earlier
                else:
                    prev.right = None                   
                    curr = curr.right
                    
        return pre  