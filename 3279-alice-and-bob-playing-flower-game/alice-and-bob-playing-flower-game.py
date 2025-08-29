class Solution(object):
    def flowerGame(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        # Count even and odd numbers for x in the range [1, n]
        even_n = n // 2
        odd_n = (n + 1) // 2
        
        # Count even and odd numbers for y in the range [1, m]
        even_m = m // 2
        odd_m = (m + 1) // 2
        
        # Calculate the total number of winning pairs
        # (odd_x * even_y) + (even_x * odd_y)
        winning_pairs = (odd_n * even_m) + (even_n * odd_m)
        
        return winning_pairs
            