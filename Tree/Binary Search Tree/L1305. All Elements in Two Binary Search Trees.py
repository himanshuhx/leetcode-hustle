class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def walk(root):
            if not root:
                return
            walk(root.left)
            inorder.append(root.val)
            walk(root.right)

        inorder = []
        walk(root1)
        walk(root2)
        inorder.sort()
        return inorder
