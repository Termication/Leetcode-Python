class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        seen = set(nums)
        while original in seen:
            original *= 2
        return original
        