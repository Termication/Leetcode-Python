class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)  # Convert the list into a heap
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)  # Remove elements until we have only k elements
        

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)  # Maintain the size of the heap to k
        return self.min_heap[0]  # The root of the heap is the kth largest element
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)