class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        min_dist = float('inf')
        for i, val in enumerate(nums):
            if val == target:
                min_dist = min(min_dist, abs(i - start))
        return min_dist
