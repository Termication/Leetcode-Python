class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        """
        Maximize the matrix sum by flipping adjacent elements.

        Args:
            matrix: List[List[int]] - n x n integer matrix.

        Returns:
            int: Maximum possible sum of the matrix.
        """
        total_sum = 0
        negative_count = 0
        smallest_abs = float('inf')

        for row in matrix:
            for num in row:
                total_sum += abs(num)
                if num < 0:
                    negative_count += 1
                smallest_abs = min(smallest_abs, abs(num))

        # If there are an odd number of negatives, adjust by removing the smallest absolute value twice
        if negative_count % 2 != 0:
            total_sum -= 2 * smallest_abs

        return total_sum
        