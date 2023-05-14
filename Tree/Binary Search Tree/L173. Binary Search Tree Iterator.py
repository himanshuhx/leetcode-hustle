class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.pushLeftNodes(root)

    def next(self) -> int:
        topNode = self.stack.pop()
        self.pushLeftNodes(topNode.right)
        return topNode.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def pushLeftNodes(self, curr):
        while curr:
            self.stack.append(curr)
            curr = curr.left

            # goto right node of next node and append every left node in stack
