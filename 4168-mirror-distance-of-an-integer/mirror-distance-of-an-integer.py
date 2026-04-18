class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        rev = int(str(n)[::-1])   # reverse digits
        return abs(n - rev)
