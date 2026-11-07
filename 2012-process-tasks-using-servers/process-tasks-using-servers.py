import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        # Available heap: (weight, index)
        available = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(available)
        
        # Busy heap: (free_time, weight, index)
        busy = []
        
        ans = []
        current_time = 0
        
        for j, task_time in enumerate(tasks):
            # Update current_time to at least the arrival time of task j
            current_time = max(current_time, j)
            
            # Move all servers that have finished processing back to available
            while busy and busy[0][0] <= current_time:
                _, w, i = heapq.heappop(busy)
                heapq.heappush(available, (w, i))
                
            # If no servers are available, jump time forward to when the next server frees up
            if not available:
                current_time = busy[0][0]
                while busy and busy[0][0] <= current_time:
                    _, w, i = heapq.heappop(busy)
                    heapq.heappush(available, (w, i))
            
            # Assign the best available server to task j
            w, i = heapq.heappop(available)
            ans.append(i)
            
            # Push server to busy heap with its new completion time
            heapq.heappush(busy, (current_time + task_time, w, i))
            
        return ans