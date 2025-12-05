class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        n = len(nums)
        if total % 2 == 0:
            return n - 1
        else:
            return 0