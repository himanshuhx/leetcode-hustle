class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def isValid(i, j, prev_value):
            if i >= 0 and j >= 0 and i < n and j < m and matrix[i][j] > prev_value:
                return True
            return False

        def dfs(i, j, prev_value):
            if not isValid(i, j, prev_value):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            count = 0

            for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                newX, newY = x+i, y+j
                count = max(count, 1 + dfs(newX, newY, matrix[i][j]))

            memo[(i, j)] = count
            return memo[(i, j)]

        memo = {}
        res = 0
        n, m = len(matrix), len(matrix[0])

        for i in range(n):
            for j in range(m):
                res = max(res, dfs(i, j, -float('inf')))

        return res
