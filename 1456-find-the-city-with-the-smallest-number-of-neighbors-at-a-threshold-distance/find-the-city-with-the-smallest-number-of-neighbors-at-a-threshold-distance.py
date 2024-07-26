class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        import sys
        inf = sys.maxsize

        # Initialize the distance matrix
        dist = [[inf] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        # Fill the distance matrix with edge weights
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        # Apply Floyd-Warshall Algorithm to find shortest paths between all pairs of nodes
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        # Find the city with the minimum number of reachable cities within the threshold distance
        min_neighbor_count = n
        result_city = -1

        for i in range(n):
            neighbor_count = 0
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    neighbor_count += 1

            # Update the result city
            if neighbor_count <= min_neighbor_count:
                min_neighbor_count = neighbor_count
                result_city = i

        return result_city