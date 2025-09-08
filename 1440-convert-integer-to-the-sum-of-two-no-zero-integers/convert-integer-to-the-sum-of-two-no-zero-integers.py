class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def contains_zero(num):
        #hlper function to check if a number contains the digit 0.
            return '0' in str(num)

        # Iterate through all possible values for the first number, a.
        for a in range(1, n):
            b = n - a
            
            # If both a and b are no-zero integers, we found a solution.
            if not contains_zero(a) and not contains_zero(b):
                return [a, b]