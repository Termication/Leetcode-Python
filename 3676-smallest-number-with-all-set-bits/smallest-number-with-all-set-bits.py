class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Get the bit length of n
        bit_length = n.bit_length()
        
        # Calculate the number with all 1s for this bit length
        candidate = (1 << bit_length) - 1
        
        # If this candidate is >= n, return it
        if candidate >= n:
            return candidate
        
        # Otherwise, we need the next number with all 1s
        return (1 << (bit_length + 1)) - 1
        