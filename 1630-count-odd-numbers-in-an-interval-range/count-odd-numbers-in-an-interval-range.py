class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        # If both ends are even, odds = (high - low) // 2
        # Otherwise, odds = (high - low) // 2 + 1
        return ((high - low) // 2) + (1 if (low % 2 == 1 or high % 2 == 1) else 0)