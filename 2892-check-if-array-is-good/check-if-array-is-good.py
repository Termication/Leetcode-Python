from collections import Counter

class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = max(nums)
        if len(nums) != n + 1:
            return False
        
        freq = Counter(nums)
        
        # Check numbers 1..n-1 appear once
        for x in range(1, n):
            if freq[x] != 1:
                return False
        
        # Check n appears twice
        return freq[n] == 2
