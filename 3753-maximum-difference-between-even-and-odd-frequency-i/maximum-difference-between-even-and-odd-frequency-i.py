import collections
import math

class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Step 1: Count Frequencies
        freq_map = collections.Counter(s)

        max_odd_freq = 0
        min_even_freq = float('inf')  # Use a very large number for initial min_even_freq

        # Step 3: Find Max Odd and Min Even Frequencies
        for char_freq in freq_map.values():
            if char_freq % 2 == 1:  # Odd frequency
                max_odd_freq = max(max_odd_freq, char_freq)
            else:  # Even frequency
                min_even_freq = min(min_even_freq, char_freq)
        
        # Step 4: Calculate Difference
        return max_odd_freq - min_even_freq