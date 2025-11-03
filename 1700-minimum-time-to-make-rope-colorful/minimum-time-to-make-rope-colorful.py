class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        total_time = 0
        n = len(colors)
        
        for i in range(1, n):
            if colors[i] == colors[i - 1]:
                # Keep track of the maximum in current consecutive group
                total_time += min(neededTime[i], neededTime[i - 1])
                # Update current balloon's time to be the maximum so far
                neededTime[i] = max(neededTime[i], neededTime[i - 1])
        
        return total_time