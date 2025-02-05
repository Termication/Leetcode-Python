class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        """
        Checks if two strings can be made equal by performing at most one string swap.

        Args:
            s1: The first string.
            s2: The second string.

        Returns:
            True if the strings can be made equal with at most one swap, False otherwise.
        """

        if s1 == s2:
            return True

        diff_indices = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_indices.append(i)

        if len(diff_indices) == 0:  # Already equal (handled above, but included for clarity)
            return True

        if len(diff_indices) == 2:
            i, j = diff_indices[0], diff_indices[1]
            if s1[i] == s2[j] and s1[j] == s2[i]:
                return True
            else:
                return False
        else:
            return False
        