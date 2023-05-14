class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def tree(i, j):
            if i>j: return None
            mid = (i+j)//2
            root = TreeNode(inorder[mid])
            root.left = tree(i, mid-1)
            root.right = tree(mid+1, j)
            return root
        
        inorder = []
        while head:
            inorder.append(head.val)
            head = head.next
            
        return tree(0, len(inorder)-1)