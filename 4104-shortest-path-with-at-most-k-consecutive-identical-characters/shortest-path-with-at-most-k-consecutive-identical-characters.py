import heapq
from collections import defaultdict

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        # Build adjacency list
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            
        # Min-heap stores: (cost, curr_node, streak)
        # Starting state at node 0 has a streak of 1 with character labels[0]
        pq = [(0, 0, 1)]
        
        # Distance table: dist[node][streak] -> minimum cost
        # Since streak ranges from 1 to k, size is n x (k + 1)
        dist = {}
        dist[(0, 1)] = 0
        
        while pq:
            cost, u, streak = heapq.heappop(pq)
            
            # If we reached the target node n - 1, return the minimum cost
            if u == n - 1:
                return cost
            
            # If we found a better path to this exact state already, skip
            if cost > dist.get((u, streak), float('inf')):
                continue
                
            for v, w in graph[u]:
                next_streak = (streak + 1) if labels[v] == labels[u] else 1
                
                # Only proceed if the new streak does not exceed k
                if next_streak <= k:
                    next_cost = cost + w
                    if next_cost < dist.get((v, next_streak), float('inf')):
                        dist[(v, next_streak)] = next_cost
                        heapq.heappush(pq, (next_cost, v, next_streak))
                        
        return -1