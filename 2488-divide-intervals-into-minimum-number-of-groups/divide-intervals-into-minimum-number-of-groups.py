class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        '''Divides intervals into the minimum number of groups such that
        no two intervals in the same group intersect.
        '''
        # Sort intervals by their starting times
        intervals.sort(key=lambda x: x[0])

        # Min-heap to track the end times of groups
        heap = []

        for interval in intervals:
            start, end = interval
            # If the current interval can be added to an existing group (no overlap)
            if heap and heap[0] < start:
                heapq.heappop(heap)
            # Add the current interval to a group (either new or existing)
            heapq.heappush(heap, end)

        # The size of the heap represents the minimum number of groups needed
        return len(heap)
            