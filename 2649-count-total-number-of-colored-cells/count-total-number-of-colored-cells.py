class Solution:
    def coloredCells(self, n: int) -> int:
        """
        Calculates the number of colored cells after n minutes.

        Args:
            n: The number of minutes.

        Returns:
            The total number of colored cells.
        """
        if n == 1:
            return 1
        else:
            return n * n + (n - 1) * (n - 1)
        