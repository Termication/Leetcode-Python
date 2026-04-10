class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        
        positions = defaultdict(list)
        
        # Collect indices for each value
        for i, val in enumerate(nums):
            positions[val].append(i)
        
        min_dist = float('inf')
        
        # Check each value with at least 3 occurrences
        for val, idxs in positions.items():
            if len(idxs) >= 3:
                # Sliding window of size 3
                for j in range(len(idxs) - 2):
                    dist = 2 * (idxs[j+2] - idxs[j])
                    min_dist = min(min_dist, dist)
        
        return -1 if min_dist == float('inf') else min_dist
