class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def count_digits(x):
            return tuple(sorted(str(x)))
        
        # Precompute all possible digit counts for powers of 2 up to 10^9
        power2_digit_counts = {count_digits(1 << i) for i in range(31)}
        
        # Check if n's digits can be rearranged to form a power of 2
        return count_digits(n) in power2_digit_counts