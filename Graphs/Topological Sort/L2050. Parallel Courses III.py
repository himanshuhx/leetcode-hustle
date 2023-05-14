class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for i in range(n+1)]
        indegree = [0]*(n+1)

        for u, v in relations:
            graph[u].append(v)
            indegree[v] += 1

        queue = deque()
        total = [0]*(n+1)
        for i in range(1, n+1):
            if indegree[i] == 0:
                total[i] = time[i-1]
                queue.append(i)

        while queue:
            node = queue.popleft()

            for adj_node in graph[node]:
                total[adj_node] = max(
                    total[adj_node], time[adj_node-1]+total[node])
                indegree[adj_node] -= 1
                if indegree[adj_node] == 0:
                    queue.append(adj_node)

        return max(total)
