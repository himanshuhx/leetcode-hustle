class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        def build_graph(times):
            def add_edge(u, v, time):
                graph[u].append((time, v))

            for u, v, time in times:
                add_edge(u, v, time)

        def bfs(node):
            heap = []
            heapq.heappush(heap, (0, node))

            while heap:
                weight, node = heapq.heappop(heap)

                for adj_node_weight, adj_node in graph[node]:
                    if cost[node] + adj_node_weight < cost[adj_node]:
                        cost[adj_node] = cost[node] + adj_node_weight
                        heapq.heappush(heap, (cost[adj_node], adj_node))

        cost = [float('inf') for i in range(n+1)]
        cost[k] = 0
        build_graph(times)
        bfs(k)

        maxi = 0
        for i in range(1, n+1):
            maxi = max(maxi, cost[i])

        return maxi if maxi != float('inf') else -1
