class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        n = len(colors)
        
        # Check from left end
        left_dist = 0
        for j in range(n-1, -1, -1):
            if colors[j] != colors[0]:
                left_dist = j
                break
        
        # Check from right end
        right_dist = 0
        for j in range(n):
            if colors[j] != colors[n-1]:
                right_dist = (n-1) - j
                break
        
        return max(left_dist, right_dist)
