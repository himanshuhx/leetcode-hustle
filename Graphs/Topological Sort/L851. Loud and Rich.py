import collections


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for i in range(n)]
        indegree = [0]*n
        ans = [i for i in range(n)]

        for u, v in richer:
            graph[u].append(v)
            indegree[v] += 1

        q = collections.deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()

            for adj_node in graph[node]:

                indegree[adj_node] -= 1
                if indegree[adj_node] == 0:
                    q.append(adj_node)

                if quiet[ans[adj_node]] > quiet[ans[node]]:
                    ans[adj_node] = ans[node]

        return ans
