class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """

        m, r = divmod(n, 7)
        full = 7 * m * (m + 7) // 2
        rest = r * (2 * m + r + 1) // 2
        return full + rest
        