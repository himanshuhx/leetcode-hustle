from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        maxi = root.val
        max_level_no = curr_level_no = 1 
        while q:
            curr_level_sum = 0
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                curr_level_sum += node.val
            if curr_level_sum > maxi:
                maxi = curr_level_sum
                max_level_no = curr_level_no
            curr_level_no += 1
        return max_level_no