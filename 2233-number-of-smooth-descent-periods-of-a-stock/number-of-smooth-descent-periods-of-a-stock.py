class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total = 1
        curr_len = 1

        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                curr_len += 1
            else:
                curr_len = 1
            total += curr_len

        return total