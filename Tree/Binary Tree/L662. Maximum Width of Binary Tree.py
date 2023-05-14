from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi = 1
        queue = deque()
        queue.append([root,1])
        
        while queue:
            maxi = max(maxi, queue[-1][1] - queue[0][1] + 1)
            for i in range(len(queue)):
                node, pos = queue.popleft()
                if node.left:
                    queue.append([node.left, 2*pos])
                if node.right:
                    queue.append([node.right, 2*pos+1])
        return maxi