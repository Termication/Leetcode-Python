class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for num in nums:
            for ch in str(num):   # convert to string and iterate digits
                result.append(int(ch))
        return result
