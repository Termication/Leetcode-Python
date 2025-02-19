class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        """
        Finds the k-th lexicographical happy string of length n.

        Args:
            n: The length of the happy string.
            k: The k-th lexicographical string to find.

        Returns:
            The k-th happy string, or an empty string if it doesn't exist.
        """

        def generate_happy_strings(current_string, length, result):
            if length == 0:
                result.append(current_string)
                return

            for char in "abc":
                if not current_string or char != current_string[-1]:
                    generate_happy_strings(current_string + char, length - 1, result)

        happy_strings = []
        generate_happy_strings("", n, happy_strings)
        happy_strings.sort()  # Ensure lexicographical order

        if k > len(happy_strings):
            return ""
        else:
            return happy_strings[k - 1]
        