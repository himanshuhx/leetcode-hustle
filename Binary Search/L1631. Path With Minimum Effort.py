from collections import deque


class Solution:
    def minimumEffortPath(self, h: List[List[int]]) -> int:
        def isValid(i, j):
            if i >= 0 and i < m and j >= 0 and j < n:
                return True
            return False

        def feasible(cost):
            q = deque()
            q.append((0, 0))
            visited = set()
            visited.add((0, 0))

            while q:
                x, y = q.popleft()
                if x == m-1 and y == n-1:
                    return True

                for i, j in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    newX, newY = x+i, y+j

                    if (newX, newY) not in visited and isValid(newX, newY):
                        if abs(h[newX][newY] - h[x][y]) <= cost:
                            q.append((newX, newY))
                            visited.add((newX, newY))

            return False

        m, n = len(h), len(h[0])
        left, right = 0, 10**6+1
        while left < right:
            mid = left + (right-left)//2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
