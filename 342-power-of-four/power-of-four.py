class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Step 1: Must be positive and a power of 2
        if n <= 0 or (n & (n - 1)) != 0:
            return False
        # Step 2: The single 1-bit must be in an odd position
        return (n & 0xAAAAAAAA) == 0