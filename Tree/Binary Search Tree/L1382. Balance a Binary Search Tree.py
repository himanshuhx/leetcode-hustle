class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def tree(i, j):
            if i > j:
                return None
            mid = (j+i)//2
            root = TreeNode(inorder[mid])
            root.left = tree(i, mid-1)
            root.right = tree(mid+1, j)
            return root

        def getInorder(root):
            if not root:
                return
            getInorder(root.left)
            inorder.append(root.val)
            getInorder(root.right)

        inorder = []
        getInorder(root)
        return tree(0, len(inorder)-1)
