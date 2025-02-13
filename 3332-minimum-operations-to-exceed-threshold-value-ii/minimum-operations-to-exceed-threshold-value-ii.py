import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap = nums.copy()
        heapq.heapify(heap)
        count = 0
        
        while len(heap) >= 2:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            
            if x >= k and y >= k:
                # All remaining elements are >= k, push back and break
                heapq.heappush(heap, x)
                heapq.heappush(heap, y)
                break
            else:
                # Combine the two smallest elements
                new_val = x * 2 + y
                heapq.heappush(heap, new_val)
                count += 1
        
        # Check if all elements in the heap are >= k
        for num in heap:
            if num < k:
                return -1
        return count
        