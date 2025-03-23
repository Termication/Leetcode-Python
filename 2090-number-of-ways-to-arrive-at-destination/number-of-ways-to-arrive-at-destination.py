class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        """
        Counts the number of ways to arrive at the destination in the shortest time.

        Args:
            n: The number of intersections.
            roads: A list of roads, where roads[i] = [ui, vi, timei].

        Returns:
            The number of ways to arrive at the destination in the shortest time, modulo 10^9 + 7.
        """
        graph = [[] for _ in range(n)]
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        distances = [float('inf')] * n
        distances[0] = 0
        ways = [0] * n
        ways[0] = 1

        pq = [(0, 0)]  # (distance, node)

        while pq:
            d, u = heapq.heappop(pq)

            if d > distances[u]:
                continue

            for v, time in graph[u]:
                if distances[u] + time < distances[v]:
                    distances[v] = distances[u] + time
                    ways[v] = ways[u]
                    heapq.heappop(pq) if (distances[v], v) in pq else None
                    heapq.heappush(pq, (distances[v], v))
                elif distances[u] + time == distances[v]:
                    ways[v] = (ways[v] + ways[u]) % (10**9 + 7)

        return ways[n - 1]
        