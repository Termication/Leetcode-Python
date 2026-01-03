class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        a, b = 6, 6  # base case for n=1
        for _ in range(2, n+1):
            a, b = (3*a + 2*b) % MOD, (2*a + 2*b) % MOD
        return (a + b) % MOD
