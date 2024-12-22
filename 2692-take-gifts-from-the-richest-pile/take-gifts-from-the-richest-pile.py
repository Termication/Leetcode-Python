class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # Create a max-heap by inserting negative values
        max_heap = [-g for g in gifts]
        heapq.heapify(max_heap)
        
        # Perform k operations
        for _ in range(k):
            # Extract the largest pile (convert back to positive)
            largest = -heapq.heappop(max_heap)
            # Reduce the pile to floor(sqrt(largest))
            reduced = math.floor(math.sqrt(largest))
            # Push the reduced pile back into the heap (as negative)
            heapq.heappush(max_heap, -reduced)
        
        # Calculate the total gifts remaining (convert back to positive)
        return -sum(max_heap)