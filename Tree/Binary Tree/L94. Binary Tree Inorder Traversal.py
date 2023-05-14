
class Solution:
    # Recursive Implementation O(N), O(N)
    def inorderTraversal(self, root):
        def dfs(root):
            if not root: return
            dfs(root.left)
            ino.append(root.val)
            dfs(root.right)
                
        ino = []
        dfs(root)
        return ino
    
    # Iterative Implementation O(N), O(N)
    def inorderTraversal(self, root):
        stack, ino = [], []
        curr = root
        while curr or stack:            
            while curr:
                stack.append(curr)
                curr = curr.left
            node = stack.pop()
            ino.append(node.val)
            curr = node.right
        return ino

    # Morris Traversal O(N), O(1)
    def inorderTraversal(self, root):
        ino = []
        
        curr = root
        while curr:
            # if there is no left print curr and move to right
            if not curr.left:
                ino.append(curr.val)
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
                    curr = curr.left
                # if we have marked it earlier
                else:
                    prev.right = None
                    ino.append(curr.val)
                    curr = curr.right
                    
        return ino