class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        """
        Checks if a number can be represented as the sum of distinct powers of three.

        Args:
          n: The input integer.

        Returns:
          True if n can be represented as the sum of distinct powers of three, False otherwise.
        """
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True