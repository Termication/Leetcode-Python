class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Count frequency of each element
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # Find the maximum frequency
        max_freq = max(freq.values())
        
        # Sum frequencies of elements with maximum frequency
        total = 0
        for count in freq.values():
            if count == max_freq:
                total += count
        
        return total