class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root):
            if not root: return 0
            left_sum = dfs(root.left)
            right_sum = dfs(root.right)
            
            curr_sum = root.val + left_sum + right_sum
            if curr_sum in sum_map:
                sum_map[curr_sum] += 1
            else:
                sum_map[curr_sum] = 1
                
            return curr_sum
        
        sum_map = {}
        dfs(root)
        ans = []
        maxi = 0
        
        for summ in sum_map:
            maxi = max(sum_map[summ], maxi)
            
        for summ in sum_map:
            if sum_map[summ] == maxi:
                ans.append(summ)
                
        return ans
        
        