import heapq
from collections import defaultdict

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Initialize the graph with the default roads
        graph = defaultdict(list)
        for i in range(n - 1):
            graph[i].append((i + 1, 1))  # Edge from i to i+1 with weight 1
        
        def dijkstra(start, end):
            # Min-heap for Dijkstra's algorithm
            min_heap = [(0, start)]  # (distance, node)
            distances = {i: float('inf') for i in range(n)}
            distances[start] = 0
            
            while min_heap:
                curr_dist, curr_node = heapq.heappop(min_heap)
                
                if curr_node == end:
                    return curr_dist
                
                for neighbor, weight in graph[curr_node]:
                    new_dist = curr_dist + weight
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        heapq.heappush(min_heap, (new_dist, neighbor))
            
            return distances[end]
        
        answer = []
        for u, v in queries:
            # Add the new road
            graph[u].append((v, 1))
            # Find the shortest path from 0 to n-1
            shortest_path = dijkstra(0, n - 1)
            answer.append(shortest_path)
        
        return answer
            