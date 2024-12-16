class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        """
        Calculate the final state of the array after k operations.

        Args:
            nums (list[int]): Input array.
            k (int): Number of operations.
            multiplier (int): Multiplier applied to the minimum value.

        Returns:
            list[int]: Final state of the array.
        """
        # Create a min-heap with (value, index)
        heap = [(value, idx) for idx, value in enumerate(nums)]
        heapq.heapify(heap)

        for _ in range(k):
            # Get the smallest value and its index
            value, idx = heapq.heappop(heap)
            # Update the array
            nums[idx] = value * multiplier
            # Push the updated value back into the heap
            heapq.heappush(heap, (nums[idx], idx))

        return nums
        