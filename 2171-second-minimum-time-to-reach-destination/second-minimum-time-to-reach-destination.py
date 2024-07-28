class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Min-heap to keep track of (time, node, count)
        heap = [(0, 1, 0)]  # (current_time, current_node, count of visits to node n)
        visited = defaultdict(lambda: [float('inf'), float('inf')])  # stores [min_time, second_min_time] for each node
        visited[1][0] = 0
        
        while heap:
            curr_time, node, count = heapq.heappop(heap)
            
            for neighbor in graph[node]:
                new_time = curr_time
                
                # Calculate the waiting time due to traffic signal
                if (new_time // change) % 2 == 1:  # if red signal
                    new_time = (new_time // change + 1) * change  # wait till it turns green
                
                new_time += time  # add the time to travel to the neighbor
                
                if new_time < visited[neighbor][0]:  # Found a new minimum time
                    visited[neighbor][1] = visited[neighbor][0]
                    visited[neighbor][0] = new_time
                    heapq.heappush(heap, (new_time, neighbor, count + (neighbor == n)))
                elif visited[neighbor][0] < new_time < visited[neighbor][1]:  # Found a new second minimum time
                    visited[neighbor][1] = new_time
                    heapq.heappush(heap, (new_time, neighbor, count + (neighbor == n)))
        
        return visited[n][1]
            