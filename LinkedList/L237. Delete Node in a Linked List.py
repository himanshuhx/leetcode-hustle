class Solution:
    def deleteNode(self, node):
        temp = node.next.val
        node.next = node.next.next
        node.val = temp