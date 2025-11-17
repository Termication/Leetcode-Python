
class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        prev = -1  # index of previous 1, -1 means none seen yet
        for i, v in enumerate(nums):
            if v == 1:
                if prev != -1 and i - prev - 1 < k:
                    return False
                prev = i
        return True