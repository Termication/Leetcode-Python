class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        """
        Check if there exists a valid binary array original
        that could have formed the derived array.

        Args:
            derived (list[int]): The derived array.

        Returns:
            bool: True if a valid original array exists, False otherwise.
        """
        n = len(derived)

        def is_valid(start):
            original = [0] * n
            original[0] = start

            # Deduce the rest of the original array
            for i in range(1, n):
                original[i] = original[i - 1] ^ derived[i - 1]

            # Check the cyclic property
            return (original[n - 1] ^ original[0]) == derived[n - 1]

        # Test both possible values for original[0]
        return is_valid(0) or is_valid(1)
            