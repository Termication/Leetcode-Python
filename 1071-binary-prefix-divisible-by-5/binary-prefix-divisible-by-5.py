
class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        result = []
        remainder = 0
        
        for bit in nums:
            remainder = (remainder * 2 + bit) % 5
            result.append(remainder == 0)
        
        return result